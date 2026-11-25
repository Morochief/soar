package main

import (
	"bytes"
	"crypto/tls"
	"encoding/base64"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"net/http"
	"os"
	"sort"
	"strings"
	"sync"
	"time"
)

const (
	defaultHost   = "technoma.stellarcyber.cloud"
	defaultEmail  = "kevinmoraes@technoma.com.py"
	defaultToken  = "rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ"
	stellarCustID = "e511c3fc54cd4d668bb67612c2ef4b04"
)

type ModuleQuery struct {
	Name  string
	Query string
}

var modules = []ModuleQuery{
	{"Firewall", "msg_class:firewall OR dev_type:fw_fortigate"},
	{"DNS Analysis", "dstport:53 OR msg_class:dns OR appid_name:DNS OR appid_name:Google-DNS"},
	{"Network Applications", "msg_class:interflow_traffic OR msg_class:flow"},
	{"Google Workspace", "msg_class:gsuite"},
	{"Plain Text Passwords", "dstport:389 OR dstport:21 OR dstport:23 OR alert_type:*password* OR msg_class:plain_text*"},
	{"All Login Failures", "action:failure OR action:failed OR msg_class:auth_failure OR event_name:*login*failure*"},
	{"Windows Logins", "win_event_id:4624 OR event_id:4624"},
	{"Windows Privilege Escalations", "win_event_id:4672 OR event_id:4672"},
	{"Windows Command Line", "process_commandline:* OR process_cmd:*"},
	{"Windows New Processes", "win_event_id:4688 OR event_id:4688 OR process_name:*"},
	{"Sophos Endpoint", "dev_type:endpoint_sophos OR msg_class:sophos*"},
	{"Non-Standard Port Usage", "appid_stdport:no"},
	{"Tunneled Traffic", "proto_name:gre OR proto_name:ipip OR dstport:4789"},
	{"Windows Account Changes", "win_event_id:4720 OR win_event_id:4722 OR win_event_id:4724 OR win_event_id:4738 OR event_id:4720"},
	{"Windows Account Lockouts", "win_event_id:4740 OR event_id:4740"},
	{"Windows PowerShell Startups", "win_event_id:4104 OR event_id:4104 OR process_name:powershell.exe"},
	{"External File Storage Access", "appid_name:*drive* OR appid_name:*dropbox* OR appid_name:*onedrive*"},
	{"Cloud Email Provider Access", "appid_name:*gmail* OR appid_name:*office365* OR appid_name:*outlook*"},
	{"Windows Login Failures", "win_event_id:4625 OR event_id:4625"},
	{"Windows Software Installed", "win_event_id:11707 OR event_id:11707"},
}

func getJWT(client *http.Client, host, email, token string) string {
	authStr := fmt.Sprintf("%s:%s", email, token)
	authB64 := base64.StdEncoding.EncodeToString([]byte(authStr))
	url := fmt.Sprintf("https://%s/connect/api/v1/access_token", host)
	req, _ := http.NewRequest("POST", url, bytes.NewBuffer([]byte("{}")))
	req.Header.Set("Authorization", "Basic "+authB64)
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
	resp, _ := client.Do(req)
	if resp == nil {
		return ""
	}
	defer resp.Body.Close()
	var authResp struct {
		AccessToken string `json:"access_token"`
	}
	json.NewDecoder(resp.Body).Decode(&authResp)
	return authResp.AccessToken
}

func esSearch(client *http.Client, host, jwt, index string, query map[string]interface{}) map[string]interface{} {
	b, _ := json.Marshal(query)
	url := fmt.Sprintf("https://%s/connect/api/data/%s/_search", host, index)
	req, _ := http.NewRequest("GET", url, bytes.NewBuffer(b))
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+jwt)
	resp, err := client.Do(req)
	if err != nil || resp.StatusCode != http.StatusOK {
		return nil
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	var res map[string]interface{}
	json.Unmarshal(body, &res)
	return res
}

type ModuleResult struct {
	Name  string
	Count int64
}

func main() {
	dateFlag := flag.String("date", "", "Fecha objetivo en formato YYYY.MM.DD (por defecto hoy UTC)")
	flag.Parse()

	host := defaultHost
	if h := os.Getenv("STELLAR_HOST"); h != "" {
		host = h
	}
	email := defaultEmail
	if e := os.Getenv("STELLAR_EMAIL"); e != "" {
		email = e
	}
	token := defaultToken
	if t := os.Getenv("STELLAR_TOKEN"); t != "" {
		token = t
	}

	tr := &http.Transport{
		TLSClientConfig:     &tls.Config{InsecureSkipVerify: true},
		MaxIdleConns:        50,
		MaxIdleConnsPerHost: 20,
	}
	client := &http.Client{Transport: tr, Timeout: 30 * time.Second}
	jwt := getJWT(client, host, email, token)
	if jwt == "" {
		fmt.Println("[-] Error obteniendo token JWT de Stellar Cyber")
		return
	}

	dateStr := *dateFlag
	if dateStr == "" {
		dateStr = time.Now().UTC().Format("2006.01.02")
	}
	targetIndex := fmt.Sprintf("*%s*%s*", dateStr, stellarCustID)

	sep := strings.Repeat("=", 95)
	subSep := strings.Repeat("-", 95)

	fmt.Printf("\n%s\n", sep)
	fmt.Printf(" 🚀 SUITE MAESTRA DE AUDITORIA: 20 DASHBOARDS + DEEP DIVE (1-CLICK)\n")
	fmt.Printf(" 📅 Fecha: %s (UTC) | Indice: %s\n", dateStr, targetIndex)
	fmt.Printf("%s\n\n", sep)

	// 1. REVISION PARALELA DE LOS 20 DASHBOARDS
	var wg sync.WaitGroup
	resultsChan := make(chan ModuleResult, len(modules))

	for _, mod := range modules {
		wg.Add(1)
		go func(m ModuleQuery) {
			defer wg.Done()
			qBody := map[string]interface{}{
				"size":              0,
				"track_total_hits": true,
				"query": map[string]interface{}{
					"bool": map[string]interface{}{
						"filter": []interface{}{
							map[string]interface{}{
								"query_string": map[string]interface{}{
									"query": m.Query,
								},
							},
						},
					},
				},
			}
			res := esSearch(client, host, jwt, targetIndex, qBody)
			var count int64
			if hitsObj, ok := res["hits"].(map[string]interface{}); ok {
				if tObj, ok := hitsObj["total"].(map[string]interface{}); ok {
					if v, ok := tObj["value"].(float64); ok {
						count = int64(v)
					}
				}
			}
			resultsChan <- ModuleResult{Name: m.Name, Count: count}
		}(mod)
	}

	wg.Wait()
	close(resultsChan)

	var sortedRes []ModuleResult
	var totalDocs int64
	for r := range resultsChan {
		sortedRes = append(sortedRes, r)
		totalDocs += r.Count
	}

	sort.Slice(sortedRes, func(i, j int) bool {
		return sortedRes[i].Count > sortedRes[j].Count
	})

	fmt.Printf("[1] 📊 RESUMEN EJECUTIVO: LOS 20 DASHBOARDS DE THREAT HUNTING\n")
	fmt.Println(subSep)
	fmt.Printf("%-35s | %-18s | %-10s\n", "DASHBOARD / MODULO", "EVENTOS REALES", "PORCENTAJE")
	fmt.Println(subSep)

	for _, r := range sortedRes {
		pct := 0.0
		if totalDocs > 0 {
			pct = (float64(r.Count) / float64(totalDocs)) * 100.0
		}
		bar := ""
		if pct > 20.0 {
			bar = "🚨 [TOP DEVORADOR DE CUOTA]"
		} else if pct > 5.0 {
			bar = "⚠️ [CONSUMO ALTO]"
		} else if pct > 1.0 {
			bar = "🔹 [MODERADO]"
		}
		fmt.Printf("%-35s | %18d  | %6.2f%% %s\n", r.Name, r.Count, pct, bar)
	}
	fmt.Println(subSep)
	fmt.Printf("%-35s | %18d  | 100.00%%\n", "TOTAL AGREGADO DE EVENTOS", totalDocs)

	// 2. DEEP DIVE EN FIREWALL
	fmt.Printf("\n\n[2] 🛡️ DEEP DIVE #1: FIREWALL (ACCIONES Y APLICACIONES MAS PESADAS)\n")
	fmt.Println(subSep)
	qFW := map[string]interface{}{
		"size": 0,
		"query": map[string]interface{}{
			"query_string": map[string]interface{}{
				"query": "msg_class:firewall OR dev_type:fw_fortigate",
			},
		},
		"aggs": map[string]interface{}{
			"actions": map[string]interface{}{
				"terms": map[string]interface{}{"field": "action.keyword", "size": 5},
			},
			"apps": map[string]interface{}{
				"terms": map[string]interface{}{"field": "appid_name.keyword", "size": 5},
			},
		},
	}
	resFW := esSearch(client, host, jwt, targetIndex, qFW)
	if aggs, ok := resFW["aggregations"].(map[string]interface{}); ok {
		fmt.Println("  • Top Acciones en Firewall:")
		if actObj, ok := aggs["actions"].(map[string]interface{}); ok {
			for _, item := range actObj["buckets"].([]interface{}) {
				m := item.(map[string]interface{})
				fmt.Printf("    - %-15s : %10.0f eventos\n", m["key"], m["doc_count"].(float64))
			}
		}
		fmt.Println("\n  • Top Aplicaciones de Red / Protocolos:")
		if appObj, ok := aggs["apps"].(map[string]interface{}); ok {
			for _, item := range appObj["buckets"].([]interface{}) {
				m := item.(map[string]interface{})
				fmt.Printf("    - %-25s : %10.0f eventos\n", m["key"], m["doc_count"].(float64))
			}
		}
	}

	// 3. DEEP DIVE EN DNS
	fmt.Printf("\n\n[3] 🌐 DEEP DIVE #2: DNS (DOMINIOS Y MAQUINAS QUE SATURAN LA RED)\n")
	fmt.Println(subSep)
	qDNS := map[string]interface{}{
		"size": 0,
		"query": map[string]interface{}{
			"query_string": map[string]interface{}{
				"query": "dstport:53 OR msg_class:dns",
			},
		},
		"aggs": map[string]interface{}{
			"domains": map[string]interface{}{
				"terms": map[string]interface{}{"field": "dstip_host.keyword", "size": 5},
			},
			"src_ips": map[string]interface{}{
				"terms": map[string]interface{}{"field": "srcip", "size": 5},
			},
		},
	}
	resDNS := esSearch(client, host, jwt, targetIndex, qDNS)
	if aggs, ok := resDNS["aggregations"].(map[string]interface{}); ok {
		fmt.Println("  • Top Dominios Consultados:")
		if dObj, ok := aggs["domains"].(map[string]interface{}); ok {
			for _, item := range dObj["buckets"].([]interface{}) {
				m := item.(map[string]interface{})
				fmt.Printf("    - %-30s : %10.0f consultas\n", m["key"], m["doc_count"].(float64))
			}
		}
		fmt.Println("\n  • Top IPs de Origen (Generadoras de Tormenta DNS):")
		if ipObj, ok := aggs["src_ips"].(map[string]interface{}); ok {
			for _, item := range ipObj["buckets"].([]interface{}) {
				m := item.(map[string]interface{})
				fmt.Printf("    - %-20s : %10.0f consultas\n", m["key"], m["doc_count"].(float64))
			}
		}
	}

	fmt.Printf("\n%s\n", sep)
	fmt.Println(" ✅ AUDITORIA INTEGRAL COMPLETADA EN UN SOLO COMANDO")
	fmt.Printf("%s\n\n", sep)
}
