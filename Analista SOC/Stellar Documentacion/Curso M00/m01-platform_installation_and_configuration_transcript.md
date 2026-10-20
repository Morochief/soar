# M01 - Platform Installation And Configuration Transcript

> **Documento Original:** `m01-platform_installation_and_configuration_transcript.pdf`  
> **Total Páginas:** 56  
> **Formato:** Transcripción / Manual de Curso Stellar Cyber Open XDR

---


<!-- Página 1 -->

 STELLAR CYBER OPEN XDR PLATFORM 
 INSTALLATION AND CONFIGURATION 
 L00  -  INTRODUCTION  .......................................................................................................................................................................  2 
 L00A-PRES:  Introduction  to  Stellar  Cyber  Platform  Installation  (04m:15s)  ................................  2 
 L00B-PRES:  High-Level  Platform  Component  Roles  (08m:05s)  ..........................................................  3 
 L01  -  ESXi  DATASTORE  CONFIGURATION  ........................................................................................................................  5 
 L01A-PRES:  ESXi  Datastore  Conﬁguration  (15m:25s)  ....................................................................................  5 
 L01B-DEMO:  ESXi  Datastore  Conﬁguration  (18m:05s)  .................................................................................  9 
 L02  -  ESXi  NETWORKING  CONFIGURATION  ................................................................................................................  13 
 L02A-PRES:  ESXi  Networking  Conﬁguration  (07m:35s)  .............................................................................  13 
 L02B-DEMO:  ESXi  Networking  Conﬁguration  (10m:00s)  ..........................................................................  15 
 L03  -  DATA  LAKE  VIRTUAL  MACHINE  CREATION  ....................................................................................................  18 
 L03A-PRES:  Data  Lake  VM  Creation  (10m:50s)  ................................................................................................  18 
 L03B-DEMO:  Data  Lake  VM  Creation  (08m:10s)  .............................................................................................  21 
 L04  -  DATA  LAKE  VIRTUAL  MACHINE  CONFIGURATION  .................................................................................  23 
 L04A-PRES:  Data  Lake  Conﬁguration  (16m:05s)  ............................................................................................  23 
 L04B-DEMO:  Data  Lake  Conﬁguration  (17m:10s)  ..........................................................................................  27 
 L05  -  DATA  ANALYZER  VIRTUAL  MACHINE  CREATION  .....................................................................................  32 
 L05A-PRES:  Data  Analyzer  VM  Creation  (08m:50s)  ....................................................................................  32 
 L05B-DEMO:  Data  Analyzer  VM  Creation  (08m:50s)  .................................................................................  34 
 L06  -  DATA  ANALYZER  VIRTUAL  MACHINE  CONFIGURATION  ...................................................................  36 
 L06A-PRES:  Data  Analyzer  Conﬁguration  (08m:25s)  .................................................................................  36 
 L06B-DEMO:  Data  Analyzer  Conﬁguration  (09m:15s)  ...............................................................................  38 
 L07  -  DATA  PROCESSOR  CONFIGURATION  ................................................................................................................  40 
 L07A-PRES:  Data  Processor  Conﬁguration  (09m:50s)  .............................................................................  40 
 L07B-DEMO:  Data  Processor  Conﬁguration  (07m:30s)  ............................................................................  42 
 L08  -  DATA  LAKE  ADDITIONAL  DRIVE  CONFIGURATION  ................................................................................  44 
 L08A-PRES:  Data  Lake  Additional  Drive  Conﬁguration  (07m:55s)  .................................................  44 
 L08B-DEMO:  Data  Lake  Additional  Drive  Conﬁguration  (11m:25s)  ................................................  46 
 L09  -  RECONFIGURING  THE  DATA  PROCESSOR  FOR  CLUSTER  ARCHITECTURE  .....................  49 
 L09B-DEMO:  Extended  Content  Reconﬁguring  the  Data  Processor  (33m:00s)  .................  49 
 ADM-01-01-224  1 


---

<!-- Página 2 -->

 L00 - INTRODUCTION 
 L00A-PRES: Introduction to Stellar Cyber Platform Installation 
 (04m:15s) 
 00:00-01:00 
 Hi and welcome to  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module. I'm David 
 Shirley from the Stellar Cyber Enablement and Training teams. The lessons in this module show how 
 to install, conﬁgure, and verify a Stellar Cyber Data Processor in VMware's ESXi hypervisor. We will 
 cover the conﬁguration of ESXi data stores, ESXi networking, the creation and conﬁguration of the 
 Data Lake and Data Analyzer virtual machines, and the ﬁnal conﬁguration in the Stellar Cyber user 
 interface. Throughout this module, there may be new concepts and terms that you may not be 
 familiar with. But that's okay and to be expected. The important thing is that you become familiar 
 with the concepts and the terms described. Throughout the Stellar Cyber Open XDR training 
 curriculum, your understanding and application of cybersecurity principles… 
 01:00-02:00 
 …will deepen with each repetition, iteration, and example. As you advance, you're on your way to 
 becoming a cybersecurity superstar. Thank you for your dedication. 
 Welcome to  Stellar Cyber Open XDR Platform Installation  and Conﬁguration  . The following lessons 
 are included in this module: 
 ●  High-level Platform Component Roles  . At a high level  we will see deployment architectures 
 and the role of the Data Lake and the Data Analyzer in a Stellar Cyber platform deployment. 
 ●  ESXi Data Store Conﬁguration  . This lesson starts  with an overview of the resource 
 requirements of the Data Lake and the Data Analyzer virtual machines followed by the 
 creation of the Data Stores in ESXi. 
 02:00-03:00 
 ●  ESXi Networking Conﬁguration.  This lesson starts  with an explanation of the basic cluster 
 architecture and the dedicated cluster architecture followed by the networking requirements 
 in ESXi. 
 ●  Virtual Machine Creation - Data Lake (DL).  With the  Data Store and networking complete in 
 ESXi, next we will download the software image and create the Data Lake virtual machine. 
 ●  Stellar Cyber Platform - Data Lake Conﬁguration  .  This lesson starts with powering on the 
 Data Lake virtual machine and then the initial console CLI conﬁguration for the Data Lake. 
 ●  Virtual Machine Creation - Data Analyzer.  In this  lesson, we create the Data Analyzer virtual 
 machine in ESXi. 
 ADM-01-01-224  2 


---

<!-- Página 3 -->

 ●  Stellar Cyber Platform - Data Analyzer Conﬁguration  . This lesson starts with powering on the 
 Data Analyzer virtual machine, followed by the initial console CLI conﬁguration for the Data 
 Analyzer. 
 03:00-04:15 
 ●  Stellar Cyber Platform - Data Processor Conﬁguration  .  With the Data Store and networking in 
 ESXi complete, and the creation and conﬁguration of the Data Lake and Data Analyzer virtual 
 machines complete. This lesson ﬁnishes the set up step in the Stellar Cyber user interface 
 from ﬁrst login to validation of the Data Lake, Data Analyzer, receivers, and sensor proﬁles. 
 ●  Data Lake - Data Lake Additional Drive  . Now that the  data processor is up and running, The 
 ﬁnal piece is to add the data store for the Data Lake to the Data Lake virtual machine and 
 then migrate the data to this new large storage directory. 
 ●  Extended Content - Reconﬁguring the Data Processor  .  This lesson demonstrates how to 
 modify both ESXi and the Stellar Cyber Data Processor to separate the communication 
 between the Data Lake and the Data Analyzer from the management and log forwarding 
 communication. 
 Now let's get going and happy learning. 
 L00B-PRES: High-Level Platform Component Roles (08m:05s) 
 00:00-01:00 
 The ﬁrst lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module is 
 High-Level Platform Component Roles  .  High-Level Platform  Component Roles  . This lesson includes a 
 high-level look at the platform components and their roles. 
 Stellar Cyber platform component for both on-prem and cloud consist of a data processor, which is 
 made up of a Data Analyzer and a Data Lake. From a Stellar Cyber sensor perspective, there are 
 modular sensors. They are both physical the photon sensors, and virtual appliances installed in a 
 hypervisor, something like ESXi or Hyper V or KVM, then we've got two server sensors. We have the 
 Windows Server sensor… 
 01:00-02:00 
 …where some Stellar Cyber software is loaded on the Windows Servers, and then the Linux Server 
 sensor where Stellar Cyber software is loaded onto the Linux server. In a cloud environment, Stellar 
 Cyber takes care of the back end so there's no need for you to be concerned about the Data 
 Analyzer or the Data Lake, that is taken care for you in the SaaS deployment of Open XDR platform, 
 but we still have the Stellar Cyber sensors, the Modular Sensor, the Windows Server sensor and the 
 Linux Server sensor. The components: So the Stellar Cyber Open XDR platform for on prem and 
 private-hosted cloud deployments if you had your own environment, your own AWS, or your own 
 Azure or your own GCP, or your own Oracle Cloud OCI. 
 02:00-03:00 
 It's called the data processor. It's got two main components that we've already spoken about, 
 installed as virtual machines. They are the Data Analyzer, and this includes the machine learning, 
 ADM-01-01-224  3 


---

<!-- Página 4 -->

 correlation, enrichment, and the cloud connectors, and then we have a Data Lake. It contains the user 
 interface, the hot storage, warm storage, does the search, the application programming interface or 
 API, and the Data Sink. The Data Sink can simultaneously sync data to the Data Lake storage and to 
 the cold storage systems. So note Stellar Cyber platform is also available as we just described as a 
 SaaS deployment where the architecture and the maintenance of the platform is managed by Stellar 
 Cyber. So the platform deployment types, so this is for an on-prem deployment. 
 03:00-04:00 
 This is not a SaaS deployment. We can deploy either as a single node deployment with the data 
 processor installed as a single Data Analyzer node and a single Data Lake node. So just one of each 
 is a single deployment. For a more scalable environment, we can deploy in a cluster deployment with 
 the data processor installed as a Data Analyzer cluster and the Data Lake as a cluster to achieve 
 higher and ingest higher data ingestion rates, greater storage capability, and longer data retention in 
 warm storage. The Data Analyzer cluster: It's a collection of Data Analyzer instances or virtual 
 machines as we've been talking about that will work together to process and analyze the data. The 
 types of Data Analyzer instances are designed as either master or worker nodes. So we have a Data 
 Analyzer master–it's the node that coordinates the clusters and manages its operation–and then we 
 have the Data Analyzer worker nodes… 
 04:00-05:00 
 …that execute the data processing tasks, and contribute to increased processing capacity and 
 resiliency. The Data Lake instance: So they're designed as a master worker and coordinating node to 
 work together to store managed data in the Data Lake. So the Data Lake master node oversees the 
 storage management and the search operations, and then the Data Lake Worker nodes handle the 
 actual storage. A coordinating node is a special type of Data Lake worker node that focuses on 
 coordinating data searches and requests from di erent services to the data nodes in the cluster, 
 improving our overall performance. So the advantage of the clustered architecture, we have 
 improved performance so we can distribute the workload across multiple nodes for faster 
 processing. 
 05:00-06:00 
 Scalability: So easily handle more nodes to handle the increased load of the data. So as the 
 deployment grows we can continue to add worker nodes to increase that scalability. High availability: 
 So redundancy ensures that the system remains operational, even if a single node fails we have built 
 in redundancy with high availability. Workload distribution: So it manages more data and enhances 
 the processing capabilities and some fault tolerance. So it continues functioning despite individual 
 node failures relates back to our high availability.  Okay  . Stellar Cyber Open XDR platform for on 
 prem and cloud has two main components. Virtual machine: So we talked about the Data Analyzer, 
 which includes the machine learning, the correlation, the enrichment of Interﬂow records, and the 
 cloud connector components. 
 06:00-07:00 
 So we have a data master or how we've written here D-A and a small m, and optional DA workers 
 within the cluster to support extra capacity. When you ﬁrst create this you don't have to have all of 
 those workers available, but we do create it from a start to say it's going to be a clustered 
 ADM-01-01-224  4 


---

<!-- Página 5 -->

 environment The Data Lake contains user interface, Data Sink, and Elasticsearch components. So the 
 Data Lake master or as a reference here DLm, and optional Data Lake workers within the cluster to 
 support extra capacity. Just a note at the bottom there that Stellar Cyber platform is available as a 
 SaaS deployment architecture where the maintenance of the platform is managed by Stellar Cyber. 
 Alright. The cluster components we've talked a little bit about these. We have a DAm or a DA Master. 
 That's the Data Analyzer master node that coordinates the activities of the worker nodes and 
 manages the overall cluster. 
 07:00-08:05 
 Then below that data master we have the worker nodes, the Data Analyzer workers. They perform 
 data ingestion from the sensors and connectors, as well as enrichment. It helps increase data 
 processing capacity and improves fault tolerance. The Data Lake Master, here DLm, that manages 
 storage and search operations in the Data Lake. It stores data itself and coordinates data searches 
 and requests from di erent data processing services. But beneath that we have Data Lake workers. 
 so that handles the actual storage of data in the Data Lake. They store the Elasticsearch data and 
 can be designated as a coordinating node to improve overall Data Lake performance. 
 The lesson,  High-Level Platform Component Roles  , is  complete. You should now be familiar with the 
 Stellar Cyber Open XDR platform components and their roles. Thank you. 
 L01 - ESXi DATASTORE CONFIGURATION 
 L01A-PRES: ESXi Datastore Conﬁguration (15m:25s) 
 00:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module is  ESXi 
 Datastore Conﬁguration. ESXi Datastore Conﬁguration. 
 Let's start by looking at the minimum system requirements for our Data Processor including the Data 
 Analyzer and the Data Lake. So we can see here, installation–and this example is for VMware's ESXi. 
 So the installation of the Stellar Cyber Platform on VMware ESXi requires the following. So the Data 
 Lake virtual machine needs forty CPU slash virtual CPUs, ﬁve hundred gigs of SSD provisioned thick, 
 and the Data Lake storage. In a production environment, twelve or more terabytes of SSD disk, again 
 thick provisioned. 
 01:00-02:00 
 And in a lab environment, our environment, or a test environment, at least two terabytes of SSD disk 
 again, thick provisioned. The Data Analyzer virtual machine the DA requires 44 CPU or virtual CPUs 
 and 500 gig of SSD. That's just for the virtual machine, again, thick provisioning. So let's look at the 
 recommended platform requirements for our Data Processor. We can see here for the Data Lake 
 highlighted, requires 40 CPU, 136 gig of RAM, and 500 gig of OS SSD disk space. And with the Data 
 Lake attached to it, another drive of twelve or more terabytes. So you can install a DA and a DL 
 virtual machines in the same datastore… 
 ADM-01-01-224  5 


---

<!-- Página 6 -->

 02:00-03:00 
 …if there is su cient space for the virtual machines and the twelve terabytes required for the Data 
 Lake's Elasticsearch data. However, Stellar Cyber recommends that the Data Lake use a dedicated 
 datastore, so one datastore for the virtual machines and a separate datastore in ESXi for the Data 
 Lake. So we can see there the host still needs to accommodate. So we can't use the entire number of 
 CPU up for the Data Lake and the Data Analyzer. We must leave some CPU and some memory for 
 the host to run–actually ESXi box to run. So the minimum requirements here So this is when we're 
 looking at a test environment or a training environment. As we can see there we can install the DA 
 and the DL. Those virtual machines in the same datastore if there's enough space, but we don't 
 recommend you do that. 
 03:00-04:00 
 So at a minimum requirement so we can see the CPU has dropped. We're now down to 16 virtual 
 CPUs. The RAM has not changed. Actually I think the RAM did go down from 136 to 128 and the disk 
 space remains the same as 500 gig and a minimum of two terabytes for that Data Lake where 
 Elasticsearch will be storing the data. So minimum platform requirements continued. Management IP 
 address for the ESXi host and all virtual machines so if we're deploying this as a standalone without 
 clustering, we only need one IP address. So one public IP address for each Data Processor for 
 management access. So when we say Data Processor that includes both the DA and the DL. So just 
 one for there. But if we deploy it in a clustered environment, we need two public IP addresses for 
 each of our DPs in a cluster. 
 04:00-05:00 
 One for the management access and one for the cluster itself, and we'll see where those two 
 addresses are used. From a ﬁrewall component so a reachability perspective of how do we reach the 
 Data Processor and how does the Data Processor reach the services it needs. So if we go to our 
 documentation, and search for ﬁrewall requirements, you will ﬁnd that there is a table. Wherever you 
 see DA or DL, and then either as a destination or as a source to make sure that the ports for those 
 protocols are opened if there is a ﬁrewall between the devices that are looking to communicate. 
 Alright So let's do the storage So we're starting to talk about datastores in ESXi. So the Stellar Cyber 
 platform is the Data Processor. Contains the DA Master virtual machine, and the Data Lake virtual 
 machine the Data Lake Master virtual machine. 
 05:00-06:00 
 So two datastores are created or modiﬁed in this instance with the correct size. So one terabyte for 
 our Stellar Cyber platform Data Processor, those virtual machines, one virtual machine for the Data 
 Lake and one virtual machine for the Data Analyzer, and then we'll need a second datastore for our 
 Data Lake storage where the Elasticsearch will go. So in lab environments we saw before with those 
 minimum requirements, that at least two terabytes can be used for that. So let's go ahead and see 
 how to actually create this in ESXi. So the ﬁrst one we're going to create here, as you can see, is the 
 name the Stellar Cyber virtual machines. This is where the Data Lake virtual machine and the Data 
 Analyzer virtual machine will be stored. So we give it a name and choose an available disk, and select 
 Next  . 
 ADM-01-01-224  6 


---

<!-- Página 7 -->

 06:00-07:00 
 Now when we do the partitioning, we will start with a full disk. We want to use the entire disk of just 
 one partition and it will show you there what the before partition looked like and what the after 
 partition looked like because this drive hasn't been used before. There is no before partition. And the 
 other thing you've got to choose is which virtual machine ﬁle system will it use depending on your 
 version of the ESXi. I would always recommend that you choose the latest VM ﬁle system for better 
 performance and scalability. So choose  Full disk  and  the latest version of VMFS and select  Next  . 
 Alright. So that's all required to create our ﬁrst datastore. So we look at the summary here and if 
 everything looks okay there we select  Finish  to complete  that setup. Alright. Now we want to add to 
 that. 
 07:00-08:00 
 So we decided it's not large enough. We want to add an extent to an existing VMFS datastore. So one 
 of our datastores we want to add to that. So we choose  Add an extent to existing VMFS datastore 
 and select  Next  . We will choose which datastore that  is that we're going to add an extent. In this 
 example, it's our Stellar platform VMs. That's where our Data Lake and our Data Analyzer will go and 
 select  Next  . From there, we select a disk. We can  only choose one at a time So from the available 
 disks we select  Next  , choose one and sorry choose  one and select  Next  to add that hard drive. In this 
 example you can see they are SSD disks to add that to the datastore. Again it will ask you do you 
 want to use the entire disk for the extent or partition of that disk. 
 08:00-09:00 
 As we can see here that before we select partition is hasn't been used before so there is no partition. 
 And afterwards it will look like one large VMFS partition that will be added to our datastore. So select 
 Next  . We'll be given a summary of what we're about  to do that we've chosen the datastore Stellar 
 platform VMs. We can see the disk that we've selected that we're going to partition the entire disk 
 and the VMFS version is number six for this. So we select  Finish  to continue, but will pop up with a 
 warning saying, do you know that you're going to override whatever is on that disk? And of course 
 we're okay with that because there's nothing on that disk. It's a new disk, so I will select  Yes  to 
 continue. Alright. So we can see here our disk has grown in size. It now has two terabytes of capacity 
 where previously it only had one terabyte. So we've added that second disk to have a greater size 
 datastore for those virtual machines that will sit there. 
 09:00-10:00 
 So we select  Storage  and  datastores  and you can see  that our VM has increased. Alright. Now we're 
 going to create another datastore. So we select  New  datastore  to create the datastore for our Data 
 Lake. Not the Data Lake virtual machine that will go on this Stellar platform VMs, but another 
 datastore where our Elasticsearch data will actually be stored. Alright. We're going to create a new 
 VMFS datastore. That's the selection we make and we select  Next  . Give it a name In this example it's 
 SC Data Lake Storage, and we have to select a disk. You can see that the list is starting to shrink as 
 we're using up the disk. We used two in that previous datastore. 
 10:00-11:00 
 ADM-01-01-224  7 


---

<!-- Página 8 -->

 Here is the beginning of the creation of this datastore by selecting one of these drives. And you can 
 see as we continue in this module, and add more drives to this datastore we can see that the list will 
 shrink as they get used up. So give it a name, select the disk, and choose  Next  . Again we'll be asked 
 the question, do we want to use the entire disk? And that's a yes and what VMFS, what ﬁle storage 
 system in this version of ESXi 7.0.3  VMFS 6 is available, and we choose that and select  Next  . Again 
 same as our Stellar Cyber virtual machine datastore. This one is going to ask you the question. Here 
 is a summary of what you've got. Click  Finish  if you're  happy with that. And we'll see now again we'll 
 get that pop up just to make sure to let you know we need a conﬁrmation that you are about to 
 overwrite any data that are on those disks. And if that's okay we select  Yes  to continue. 
 11:00-12:00 
 Okay. So now we have two datastores. We have our Stellar Cyber platform VMs. That's the ﬁrst one 
 we created, and then we added a second disk to it. So it's now got two terabytes of storage, and 
 we've just newly created the Stellar Cyber Data Lake storage datastore. Now we've got two of them. 
 You can see the capacity of the SC Data Lake storage is only 1.75 terabytes, so certainly not enough 
 for even a test environment or a demo environment and certainly nowhere near enough for a 
 production environment. So let's go ahead and increase the capacity of the Data Lake store. We do 
 that by selecting the name of that. We have this menu that we can see here. So along the top we 
 don't want to register a VM. We don't want to browse the datastore. We don't want to refresh or we 
 don't want to do the actions we want to select  Increase  capacity  . 
 12:00-13:00 
 This is where we'll start choosing drives to add to this datastore. Select increase capacity. It could ask 
 you how would you like to increase that capacity? and we're going to add an extent to an existing 
 VMFS datastore. So we choose the top option and select  Next  . Here is our list of disks that are 
 available to choose from to add to that datastore and remember they must be SSD disks. So if there 
 was a selection of disks available on this host we're going to choose our SSD disks to add to this 
 datastore. So choose one and select  Next  . Okay. It's  going to ask you what sort of conﬁguration do 
 you want for this disk. We're going to use again the entire disk in a VMFS 6 format, and we're going to 
 then select  Next. 
 13:00-14:00 
 We'll be given a summary of what we're about to do. So for the SC Data Lake storage datastore, 
 we're adding that disk and with a partition of using the full disk and a VMFS version of number 6. 
 We'll be given a last chance to say, “Are you sure we're about to erase all of the content that is on 
 that disk?” And if we are sure we select  Yes  to continue.  Alright. So here's a summary of what we've 
 got. Now we can see here that we now have two extents or two disks have been added: extent zero 
 and extent one. They're the ﬁrst two we've added. One was when we created, and then we just added 
 the second one previously. We're going to keep increasing that capacity. Just continue to go through 
 those steps until the datastore is the capacity that you need it to be. It's just a matter of repeating 
 those steps. 
 14:00-15:00 
 ADM-01-01-224  8 


---

<!-- Página 9 -->

 So select the datastore, click  Increase capacity  , and then select a drive. Choose the full disk, choose 
 the VMFS storage type, and then continue. So we've been around in circles and around in circles. We 
 didn't show you all of the individual pieces, but you can now see after adding disks and adding disks 
 we can now see a capacity of more than twelve terabytes. So for a production network or production 
 deployment of our Data Processor, this is a great result. We have datastore Stellar platform VMs 
 where we will host our Data Lake VM and our Data Analyzer VM. Remember, they both needed a 
 minimum of 500 gig of disk space, so two terabytes. There's plenty of space, nearly more than 
 double available for that. 
 15:00-15:24 
 And for the storage of our data, we have a di erent datastore SC Data Lake storage and we can see 
 for a production environment of more than twelve terabytes that is ready to go as well. So all 
 complete here from a datastore conﬁguration in ESXi. The lesson ESXi datastore conﬁguration is 
 complete. Thank you. 
 L01B-DEMO: ESXi Datastore Conﬁguration (18m:05s) 
 00:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module is  ESXi 
 Datastore Conﬁguration. ESXi Datastore Conﬁguration  .  In this lesson, we'll cover the system 
 requirements for installing a Data Lake and Data Analyzer virtual machines in VMware ESXi. We'll 
 also create two datastores in ESXi, one for the virtual machine images, and the other for the Data 
 Lake storage. 
 Let's start with the system requirements for installing a Data Lake and Data Analyzer virtual 
 machines in VMware ESXi. Let's go to the documentation for that and I’ll show you where it is. So here 
 we are. First thing I want to point out is that we are looking at the 4.3.7 documentation. 
 01:00-02:00 
 5.1.1 for on prem is available. But at this stage, what we want to do is install 4.3.7 so we have the 
 opportunity to show an upgrade in a later lesson. We'll start with 4.3.7. For the install of a Data 
 Processor on ESXi, we'll go to  Installing  . Hit the  drop down. (Select)  Installing a Data Processor  ,  hit 
 the drop down. You can click on the link and it will just populate the page. It's just a little slower doing 
 it that way. I prefer to go down here. The one we're going to do is (titled)  Installing a Data Processor 
 in VMware (Cluster)  as opposed to installing an all  in one where it's bundled together into one VM 
 image. We're going to do the more scalable installation in VMware where we have the option of 
 either doing a basic or a cluster installation. We'll click on that. 
 02:00-03:00 
 Before you begin–there's a couple of before you begins and we want to talk about that. A dedicated 
 ESXi server running eight seven or six dot seven. We are running. If we go to  Help  and  About  , we are 
 running 7.0.3, ESXi version 7.0.3. We ﬁt with our 7.0 right there. 6.7 is the oldest one we'll support and as 
 we know ESXi 8.0 is the latest ESXi available right now. Okay. We'll go through these. There are a 
 couple of requirements depending on the installation. If we do a non clustered or it's often called a 
 ADM-01-01-224  9 


---

<!-- Página 10 -->

 basic installation, we only need one public IP address to access the Stellar Cyber platform. If we do a 
 clustered environment, we will need two public IP addresses. 
 03:00-04:00 
 We're going to install this in a clustered environment to start with. We're going to install the basic 
 conﬁguration where we have two VMs: a Data Lake and a Data Analyzer. It just comes down to–we'll 
 go through that description–it just comes down to how many virtual switches we have. What that 
 means is, “Do we have a virtual switch for communication between the Data Lake and the Data 
 Analyzer?” or, “Is the Data Lake, Data Analyzer communication happening on the same virtual switch 
 as the ingress of data from the network?” whether log forward data or network tra c data and of 
 course management of the platform also will come in through that virtual switch. I'll specify that out a 
 bit more as we go through this conﬁguration. Okay. Ports are particularly important. What ports do 
 we need to open our ﬁrewall if we click on there? Let's have a look. What we're interested in is the DA, 
 the Data Analyzer… 
 04:00-05:00 
 …and the Data Lake, and the DP. They're all the ones we need to look at when we talk about this 
 down the bottom. We'll go look in this column. We've got our source DA DL, And this is what is it 
 communicating to? We've got a DL communicating to a mail server. Our data platform is able to 
 send emails whether that's from an ATH playbook, which we'll cover in another lesson. We'll need to 
 have these ports open for that to communicate a DA to who is needs port 43 on TCP. Then we come 
 further down to an OKTA server: Where does that need to go to? NTP server: Where does that need 
 to go through? Port twenty three UDP. There's our ﬁrewall ports that we need to have open for our 
 data on to be able to communicate. Minimum requirements are very important. Okay. We've got a 
 couple of requirements here. The ﬁrst version of the requirements is a production environment. 
 05:00-06:00 
 You can see this is recommended for production. What we need here–we can see we've got resource 
 of CPUs virtual CPUs, what's going to happen on the host to that host? Meaning our ESXi host, 44 
 physical or 88 cores with hyper threading, the DL will require 40 of those, and the DA 44 of those. 
 From a RAM perspective, the Data Lake 136 gig, the Data Analyzer, 64 gig. Then the disk space when 
 that OS is for the operating system, there are VMs. It was all going to have a virtual machine for the 
 Data Lake and a virtual machine for the Data Analyzer. We can see there we need one terabyte of 
 data. Five hundred gigs each: 500 for the DL and 500 for the DA. Okay. Moving on to the Data Lake 
 disc space. You can see there we need 12 terabytes for a production version of the Data Lake. 
 06:00-07:00 
 Now if we go a little further down in this table, we can see minimum conﬁgurations for separate DP 
 VMs. What we mean by separate is a separate Data Lake and a separate Data Analyzer virtual 
 machines. We can see there at the low end, we can have 16 CPUs for the DA, 16 for the DL. RAM we 
 still need a lot of RAM for that Data Lake 128 gig, and 64 gig is the same for the Data Analyzer, but 
 what has not changed at all is the operating system space for our virtual machine. They're still 500 
 gig each. But the big change is the Data Lake. Now this would be if you were doing this in as we are, a 
 demonstration environment or a training environment, you can see the Data Lake needs at least two 
 ADM-01-01-224  10 


---

<!-- Página 11 -->

 terabytes for the Data Lake. We'll actually conﬁgure it with a little bit more than that, but we probably 
 won't go up to the 12 that's required even though we've got the space. 
 07:00-08:00 
 We'll add a few disks too, at least certainly get it over the two terabytes. Okay. The next thing we 
 need to do we've of course we've installed VMware ESXi. Let's go on a little tour of that just now. As 
 we saw before we're running 7.0.3. We can go to  Help  and then  About  and see that we're running 
 7.0.3. This has only just been created. If we have a look we can see this is a–it's got 44 CPUs. If we 
 expand that out we'll see that logical processors– there's actually 88 of them. Memory–there’s a heap 
 of memory–256 gig of memory, and there is a bunch of storage in here. Let's have a look at what 
 we've got. Virtual machines: No virtual machines so far. We still must create that Data Lake virtual 
 machine and a Data Analyzer virtual machine. 
 08:00-09:00 
 Storage: At the moment there is only one datastore. This is being called the HDD datastore. This was 
 a non SSD drive. I don't know if I mentioned that earlier, but all Data Lake and OS versions must run 
 on SSD drives. We must have that speed for input output. So this datastore, we won't use this for the 
 DL or the DA or certainly not for the Data Lake storage. This is just a non SSD. We'll create two 
 datastores: one for the virtual machines, and we'll create a second datastore for the Data Lake. If we 
 actually go and have a look at the devices we can see there's a bunch of devices in here that are 
 ready to go. Here's all of our SSD disks. We've got 1, 2, 3, 4, 5, 6, 7, 8 of them. They're all 1.75 terabytes. 
 We'll probably use…well we only need one of these for the VM storage. Remember they were 500 
 gigs each. We need at least two of them to get over the two terabyte limit for the Data Lake storage. 
 09:00-10:00 
 Maybe we'll do three or four of them just so you can see what that process looks like. From a 
 networking perspective, let's have a look at what we've got. A bunch of NIC cards on the physical 
 machine. Virtual switches: just what's come standard with it. We can see the standard vSwitch0 is 
 there by default. There's one virtual switch and the port groups that are connected to that. We've got 
 a VM network, and we've got a management network. Again, two default port groups that are using 
 vSwitch0. Okay. We're going to conﬁgure that storage. Of course we're going to increase capacity 
 and walk through how to do all that. Here's the documentation that will walk you through that, 
 creating the datastores, verifying the datastore's discs, and then actually going ahead. We won't go 
 into the actual console to do that. 
 10:00-11:00 
 What we want to do is then deploy our virtual machines: our DL master and our DA master is what 
 we want to do. We've talked a little bit about it before–the di erence in deployments. We're going to 
 do a basic deployment, which just means there's one virtual switch. We'll create a virtual switch to do 
 that or maybe we'll use vSwitch0. It’s not important. Perhaps later we will upgrade this deployment to 
 a cluster environment so we can see what that looks like with having a second virtual switch. You can 
 see that down there. We've got a second virtual switch or a cluster virtual switch there. Let's go ahead 
 and create those two datastores. Back to storage. Select  Storage  over here. We can see we had a 
 ADM-01-01-224  11 


---

<!-- Página 12 -->

 bunch of devices available. We have just the one datastore. We're going to create two more right 
 now. Let's go ahead and do that. Alright. 
 11:00-12:00 
 To do that we click on  New datastore  . The ﬁrst thing we're going to do is select  Create new VMFS 
 datastore  . That's what we want to do. We're not going  to add because we don't have anything to 
 add and we're not going to mount an NFS one, we’re going to create it on this device. Let's create the 
 ﬁrst one, the smaller one. Let's create the datastore that's going to house the virtual machines. We 
 choose  Next  . Give it a name, and our name can be something  like, how about that Stellar Cyber VMs. 
 We can use that as our name for this datastore and we choose a disk. We said there were eight of 
 them to choose from–one, two, three, four, ﬁve, six, seven, eight SSD disks all 1.75 capacity. We'll just 
 choose the ﬁrst one. There's no need to pick one or the other here. Select  Next  . Now it's going to  ask 
 what's going to happen here. We want to use the full disk. So maybe it was partitioned before but 
 these are fresh disks so there's no partitioning… 
 12:00-13:00 
 …and which ﬁle system this VMFS stands for VMware ﬁle system. You can see we have a choice 
 between ﬁve and six. We'll choose the latter one that has better performance. Select  Next  . It gives  us 
 a summary of what's going to happen. We're going to create a VM machine called Stellar Cyber VM. 
 It's going to use that disk. It's going to use the entire disk and the virtual machine ﬁle system. I think I 
 called it VMware before, the virtual machine ﬁle system version is number six for this installation of a 
 datastore. Then click  Finish  . We'll get a conﬁrmation  here that will say we're about to wipe this disk. 
 Are you sure you want to do this? Yes, we are. Okay. That's going to go ahead. We can see down at 
 the bottom. Wow! That was really quick. Create the VMFS datastore. It just does a quick rescan, all 
 successful, and we are ready to go. We can see up here we now have a datastore that says Stellar 
 Cyber VMs. It's an SSD datastore with 1.75 terabytes, which is plenty for what we need. 
 13:00-14:00 
 We only needed 500 gigs for each of those virtual machines. Now let's create the next one, the 
 datastore that we're going to put our Data Lake storage on. Again, (select)  New datastore  , (and then 
 select)  Create a new VMFS datastore  .  (Select)  Next  .  We're going to call this one, why don't we call 
 this Stellar Cyber Data Lake. Let's call it that. You can see now we've only got one, two, three, four, 
 ﬁve, six, seven. There's only seven disks left. I probably didn't have to count them. I could've used the 
 seven items over there. We'll just select one of them, and then select  Next  . Same as before–use the 
 entire disk and virtual machine ﬁle system number six. Select  Next  . There's our summary. 
 14:00-15:00 
 Our datastore name is going to be Stellar Cyber Data Lake, the disk gets chosen. The partition is to 
 use the entire disk, and the virtual machine ﬁle system version is number six. Select  Finish  . We'll  get 
 that same conﬁrmation: You sure you want to wipe the disk? Yes, we do. O  it goes and creates that. 
 Great. Now we've got two datastores, but we remember before the capacity for the Data Lake 
 storage of 1.75 is not enough. We need to add some more disk to do that. The way we would do that 
 is select the datastore. We're going to select Stellar Cyber Data Lake. There's a button up here 
 ADM-01-01-224  12 


---

<!-- Página 13 -->

 Increase Capacity  . Select that. We're going to choose to  Add an extent to an existing virtual 
 machine ﬁle system datastore  or VMFS datastore. Select  Next  . It's going to go look to see what's 
 available. Now we're down to six. 
 15:00-16:00 
 We're going to choose one of those disks. Next, same as before: full disk, VMFS number six. Select 
 Next  . There's our summary. Select  Finish  . With a conﬁrmation  we're about to wipe it. Now it's going to 
 add that second disk to the Data Lake datastore. O  it goes down here. We can see down the 
 bottom: Extend VMFS datastore, Completed successfully. If we go back to our storage, we can see 
 that our Data Lake now has a capacity of 3.49 terabytes. That's enough. That's more than the two 
 minimum, but just for safekeeping and just to do it one more time, let's open up that Data Lake and 
 we'll just add one more. Same again. Select  Add an  extent to an existing VMFS datastore  . Yes. 
 That's what we're doing. Select  Next  . Here comes the  list of disks available. We're down to ﬁve. Just 
 choose the top one. (Select)  Next  to continue. 
 16:00-17:00 
 Same again. Use the entire disk with that ﬁle system. What it would look like before, what the petition 
 would look like after You can see all free space here. Afterwards it's all going to be used by VMFS. 
 Next, there's our summary, (select)  Finish  . Yes, we  want to wipe that disk. Conﬁrm. Now back to our 
 storage. We can see our Data Lake has now grown to 5.24 terabytes, so there’s plenty of space for 
 our training environment. If go in and really look at the details of this, it'll show you the three extents 
 here. Are those three physical disks that are being used to create that storage. Just to conﬁrm, we 
 had the original HDD datastore. That was a non SSD drive, 500 gigs. We're not going to use that. 
 17:00-18:05 
 We created the Stellar Cyber VMs datastore. That's where we will put the virtual machines for a Data 
 Lake and a Data Analyzer. Then we created another datastore: Stellar Cyber Data Lake. That's where 
 we will create the storage for the Data Lake information will be stored there. We'll go see what this 
 then looks like once we boot these machines up and conﬁgure them and see how we then include the 
 use of that Data Lake storage in the DL VM. We'll see that through the system UI. 
 That's it for creating our ESXi for the moment, our datastore. 
 The lesson  ESXi Datastore Conﬁguration  is complete.  You should now be familiar with the system 
 requirements for installing Data Lake and Data Analyzer virtual machines in VMware ESXi, as well as 
 how to create datastores in ESXi. 
 L02 - ESXi NETWORKING CONFIGURATION 
 L02A-PRES: ESXi Networking Conﬁguration (07m:35s) 
 00:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module is  ESXi 
 Networking Conﬁguration. 
 ADM-01-01-224  13 


---

<!-- Página 14 -->

 ESXi comes with some default network conﬁguration that we can use. And then there's some 
 additional conﬁguration that we'll talk about that we'd like to conﬁgure in ESXi for our deployment. 
 Depending on what type of deployment you have, whether it's a basic architecture deployment or a 
 clustered architecture deployment, will depend on what conﬁguration steps we need to do within 
 ESXi. Let's go ahead and look at what the requirements are and then how to do that conﬁguration. By 
 default, vSwitch0 is a virtual switch in ESXi that is there from default. 
 01:00-02:00 
 When you ﬁrst conﬁgure ESXi on a box, on a host, the vSwitch0 will be there. We can use that for the 
 management network to access the Stellar Cyber platform. You could, as the note says down below, 
 you could optionally create a new vSwitch for the management network instead of using vSwitch0, 
 but you can just use vSwitch0. There is a port group that we could use. We can either create a new 
 port group or we can use a port group. What we want to talk about here is that we have our Data 
 Processor made up of a Data Analyzer and a Data Lake. They both need to have a network 
 interface. Those virtual machines will need to have a network interface so that they can 
 communicate. In this diagram they're going to communicate via the vSwitch0, the virtual switch inside 
 of ESXi. We can see there is a physical NIC: vmnic0 that is bound to vSwitch0, and that allows us to 
 communicate with devices outside of the ESXi host. 
 02:00-03:00 
 Devices like connectors or modular sensors. To bring information in from the physical network, they'll 
 come in via that management switch via a physical network adapter. In this case, vmnic0 into our 
 virtual switch called vSwitch0, that then will have two interfaces, two port group interfaces, from the 
 Data Analyzer and the Data Lake so that all that communication can happen. In a clustered 
 environment, so we have a dedicated networking component for a clustered environment, we can 
 see here vSwitch0 is still going to be used but this time it's only going to be used to bring data in and 
 to manage the Data Processor. 
 03:00-04:00 
 For the DA and the DL, the Data Lake and the Data Analyzer, for those two virtual machines to 
 communicate, in this example there is an additional virtual switch that's been created. This one's 
 called vSwitch-Cluster. It's just a name. You can call it whatever you like. A new port group that the 
 Data Analyzer and the Data Lake will use. And that network diagram it's called Stellar Cluster 
 Network. And you can see that is attached to an outside physical switch via vmnic1. All of the 
 conﬁguration at the top of this diagram remains the same with vSwitch0 and vmnic0 and the port 
 group of VM network. But below that in the bottom half of that diagram we've created an additional 
 vSwitch, an additional port group with another physical NIC bound to that virtual switch to talk to that 
 cluster switch. 
 04:00-05:00 
 Now on that cluster switch in the previous lessons we talked about having worker nodes for the Data 
 Lake and a worker node for the Data Analyzer and coordinating nodes for the Data Lake. They could 
 sit o  that cluster switch on another ESXi host. That's what gives us our scalability and redundancy in 
 ADM-01-01-224  14 


---

<!-- Página 15 -->

 there. They all need to communicate and in this example they would communicate via a separate 
 network as opposed to what's coming in through vSwitch0, which will be management of the data 
 platform and our security and networking data coming from those devices either from log 14 or from 
 connectors they will come in via that management switch. We can see here in the left side of our slide 
 we've got a switch vSwitch0, which is by default and we're going to use that for the management of 
 the device. We've got a vSwitch cluster for the tra c between the Data Lake master and the Data 
 Analyzer master… 
 05:00-06:00 
 …and the cluster worker nodes and maybe a coordinating node as well for the Data Lake. We're 
 going to create two new port groups. There's a port group for up the top. We can see it's port group 
 VM network, and the bottom part of that network, for VM Switch cluster, we will have a port group 
 called Stellar Cluster Network. E ectively in this architecture, the virtual machines will have two 
 network interfaces where in the previous one they only had one network interface. How do we go 
 ahead and create this? Okay. The ﬁrst thing they're doing here is creating the port group in ESXi. The 
 Stellar management network is what's being created here. We can see we access the UI of ESXi. We 
 select  Networking  , select the  Port Groups  tab, and  select  Add port group  . 
 06:00-07:00 
 This pop-up window will appear. We've got to give it a name. Stellar management network. You could 
 call it SC management network. It's just a name. That's just the name of the port group VLAN. We 
 don't need a VLAN ID in this but what's important is the virtual switch that's been selected. Now by 
 default, the ESXi host only has one virtual switch, which is vSwitch0 and that's what's been selected 
 here. We type in a name, we choose the virtual switch, and select  Add  . Then you'll see a summary of 
 what was of the port group you've created. We can see there that we are connected to vSwitch0 and 
 you can see that physical adapter connected in there vmnic0. Alright. Our port group now we have 
 Stellar management network as opposed to the default port group, which is management network. 
 07:00-07:35 
 I say default as in that's what comes with ESXi. We've got our management network, for VMware ESXi 
 management. We've got a Stellar management network and we're going to use that to access the 
 Stellar Cyber platform. Then we're going to create a Stellar cluster network, and that will be used for 
 internal communication between the Data Analyzer and the Data Lake. 
 The lesson,  ESXi Networking Conﬁguration  , is complete.  You should now be familiar with ESXi 
 networking conﬁgurations. Thank you. 
 L02B-DEMO: ESXi Networking Conﬁguration (10m:00s) 
 00:00-01:00 
 The next lesson in the  Open XDR Platform Installation  and Conﬁguration  module is  ESXi Networking 
 Conﬁguration. ESXi Networking Conﬁguration  . In this  lesson, we'll conﬁgure the ESXi networking 
 component, the virtual switches, and the port groups acquired for the DP install of a Data Lake and 
 the Data Analyzer. 
 ADM-01-01-224  15 


---

<!-- Página 16 -->

 Let's start with the conﬁgure, the networking components, vSwitches, and port groups. Alright. First of 
 all let's look at let's go back to our documentation. We are doing 4.3.7, (select)  INSTALLING  , and then 
 we're installing a data processor, and we're installing a data processor in VMware (cluster). Now even 
 though it says cluster, we'll describe what we mean by the di erence of those two. 
 01:00-02:00 
 We have these. We have basic deployment, all VMs on the same port group. We've got cluster 
 deployment where we can see separated cluster management and SPAN tra c. Let's ignore SPAN 
 tra c for the moment. We covered that in Modular Sensor in a di erent lesson. Let's just focus on 
 our DL and DA and of course the management of the platform. If you click on these graphics, they'll 
 expand them out. I'll just describe what we're seeing here. What we're seeing here is vSwitch0. We 
 saw that in the previous lesson. That is the default switch in ESXi. We'll go into ESXi and do all of this. 
 We can see we have the Management Network. That is the name of the port group that is attached 
 to this virtual switch. And then it's also attached to VM NIC0. It may not be vmnic0. It could be a 
 di erent network interface card… 
 02:00-03:00 
 …but this is a physical interface card that goes out to an external switch where there could be 
 modular sensors, there could be network tra c, there could be log forwarding tra c will come in via 
 this switch into our physical NIC that's connected to our virtual switch zero, which has a port group 
 that's called Stellar Management Network. That interface–the port group–is used by the Data Lake 
 Master, the Data Analyzer Master. Let's just ignore this SDS for the moment. That's the equivalent of 
 our Modular Sensor. That's what they mean by the SPAN tra c. What we're seeing here really is that 
 the Data Lake and the Data Analyzer are using the same virtual switch. They're actually also using 
 the same port group in VMware to communicate to the utilizing vSwitch0… 
 03:00-04:00 
 …the same switch that then goes out to the network. That's the basic deployment, and that's what 
 we're going to do to start with. Then we'll upgrade it in another lesson or maybe at the end of this 
 lesson, to the next version. Let's have a look at that. The next version of this deployment is this cluster 
 deployment. If we look at that, we can see that there is a vSwitch for cluster with a Stellar Cluster 
 Network as a port group. So just think as one as an interface and one is a switch. Let's ignore the 
 vSwitch SPAN. This is all talking about using it if we had an integrated meaning that there is a 
 Modular Sensor also in our network design. We've already seen what that looks like in a previous 
 lesson. Let's look at what this network looks like. We've got the same thing. We've got a switch 
 coming in. We've got an external switch connected via vmnic0. That's a physical port that comes into 
 virtual switch zero. 
 04:00-05:00 
 That has the port group Stellar management network that talks to our Data Lake master, our Data 
 Analyzer master. If we were to manage it via the UI, that's the interface we'd come in through. So if 
 our laptop was out here plugged into our switch coming through the physical interface into vSwitch0, 
 which is our virtual switch. We arrive at our Port Group. It is called our interface that's called Stellar 
 ADM-01-01-224  16 


---

<!-- Página 17 -->

 management network. It's really unfair to call it Stellar Management Network. It's not really a 
 network. This is a port group in this example. That's how we communicate to our DL Master and our 
 DA master. But the di erence here is the communication between the DL and the DA. There's a lot of 
 communication that happens between the two, the Data Lake and the Data Analyzer, happens on 
 another virtual switch. 
 05:00-06:00 
 This is a virtual switch called vSwitch-Cluster. Just like we've got vSwitch0, which is the default virtual 
 switch in ESXi, another switch has been created called vSwitch-Cluster, and that allows these two 
 devices, the DLm and the DAm these two virtual machines, to communicate on a di erent virtual 
 switch. All of the communication that's happening there for a more scalable environment is not 
 happening on the same interfaces that the data is arriving. The actual security and network data is 
 arriving into our data platform. They're communicating on a di erent virtual switch with a di erent 
 port group there. Now the reason that this one then has an external for itself is like, well if we've got a 
 DL master and a DA master and they're very happy communicating over their shared port group, on 
 their own virtual switch called vSwitch cluster, why would we need an external? 
 06:00-07:00 
 Well, if we think about expanding this where we have multiple DA VMs and DL VMs, we start talking 
 about worker nodes in a much bigger environment where we scale, those other virtual machines may 
 well be in an entirely di erent physical ESXi box. They all need to talk to each other. We would have 
 an external switch with an entire another deployment of ESXi with a virtual switch with VMs and port 
 groups to allow all of them to communicate where we can have a much more scalable environment. 
 That's the reason for having this external portion of this picture out to another network. Okay. That's 
 the theory on it. Let's go and set this up. Let's look at least what we have set up in ESXi. Okay. There's 
 our storage. 
 07:00-08:00 
 We're all okay then. Nothing to do there right now. We can collapse that down. We're interested in the 
 networking on this host. From a networking perspective, let's start at the bottom. We've got some 
 physical NICs. We can see that vmnic0 is the only one of these NICs that's plugged in and is up 
 running at a thousand megabits or one gig full duplex. We'll see where vmnic0 is bound. Let's look at 
 virtual switches. We have one virtual switch. vSwitch0. If we go look at vSwitch0, we get a bit of a 
 network diagram here. We can see that the topology here is that the physical NIC, vmnic0, is 
 attached to this virtual switch called vSwitch0. We have at the moment two port groups attached to 
 this virtual switch. 
 08:00-09:00 
 We've got VM network, and we've got management network. We're going to leave those two alone, 
 and we're going to go create our own port group on this. If we go back to networking and port 
 groups, we can see there are those two port groups: VM Network and management network. They're 
 both using vSwitch0. We're going to create an additional port group called Stellar Cyber 
 Management. We're going to use that interface for our basic deployment. Remember we're going to 
 start o  doing this basic deployment. We can use vSwitch0. We're going to create this port group, 
 ADM-01-01-224  17 


---

<!-- Página 18 -->

 Stellar management network, and that will be the interface that will be used for those two virtual 
 machines. Let's go to  Add port group  . We said we would  call it Stellar Cyber management. The only 
 thing we have to choose is what virtual switches are connected to. 
 09:00-10:00 
 Well, there's only one conﬁgured so far: vSwitch0. That's it. Select  Add  . That will go ahead. We'll  see it 
 down at the bottom, updating network conﬁguration. It's going to refresh it all happily. Completed 
 successfully and we can now see we have Stellar Cyber management, port group, bound to vSwitch0. 
 We are ready now to go ahead and build our VMs, our Data Lake VM and our Data Analyzer virtual 
 machine. Let's go do that. 
 The lesson,  ESXi Networking Conﬁguration,  is complete. You should now be familiar with conﬁguring 
 the ESXi networking component, the virtual switches, and the port groups acquired for the DP install 
 of a Data Lake and a Data Analyzer. Thank you. 
 L03 - DATA LAKE VIRTUAL MACHINE CREATION 
 L03A-PRES: Data Lake VM Creation (10m:50s) 
 0:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration 
 module is  Virtual Machine Creation Data Lake. Virtual  Machine Data Lake  . In this lesson we 
 will download the software image and create the Data Lake virtual machine. 
 Let's look at some of the requirements for the Data Lake and in this case the Data Analyzer 
 of what we need to do to prepare for the creation. We've already prepared our ESXi host 
 with datastores and with networking. We've created a datastore for the virtual machines. 
 We've created a datastore for the Data Lake for the data of the Data Lake. We've created 
 some networking infrastructure for both of the virtual machines. 
 01:00-02:00 
 Okay. To prepare, we talked about opening the ports on your ﬁrewall to their requirement. 
 This image is brought straight out of our documentation. Contact Stellar Cyber Support for 
 login credentials and your one-time password, which is also known as the license key. The 
 credentials will allow us to download the software required and the OTP, or the license key, 
 is what will license the software once we install it. So we will need that. Then we're going to 
 download with the credentials we've received from support, an OVA ﬁle. That OVA ﬁle is 
 used to install the same ﬁle is used to install our Data Processor. I mean by same ﬁle, the 
 same ﬁle will be used for the Data Analyzer as would be used with the Data Lake. Now we 
 can see there, there's our link, our https://acps.stellarcyber.ai/release. 
 ADM-01-01-224  18 


---

<!-- Página 19 -->

 02:00-03:00 
 In this example, we've got 4.3.7, but if you were trying to install either a previous or a later 
 release, you just replace the 4.3.7 with 5.1.1 if you were doing 5.1.1. In the example we use in 
 the demonstrations of this we've intentionally used 4.3.7 so we can show the upgrade 
 process to 5.1.1. In this example, we're going to use 4.3.7 and download that OVA ﬁle. An OVA 
 ﬁle is a ﬁle that has a bunch of components already in it that's ready to be deployed in our 
 VMware ESXi environment. To do that, we navigate to get to this image. We navigate to the 
 Knowledge Base and then go to  INSTALLING  |  Installing  a Data Processor  , and then 
 Installing a Data Processor in VMware  in a cluster  environment. We go there to locate this 
 download link and we pull that down. 
 03:00-04:00 
 Now that we've got our software, we go into the user interface of ESXi to create the virtual 
 machine. The ﬁrst one we're going to create here is our Data Lake. We've got the 
 networking that's already been conﬁgured. We have the datastores that have already been 
 conﬁgured. Now we're conﬁguring the virtual machines. In this instance from the left panel 
 we choose  Virtual Machines  , and then from the top  we select  Create / Register a virtual 
 machine  , and we will get the next pop up. Okay. The  pop up. How are we going to create 
 this virtual machine? Well we've downloaded an OVA ﬁle. We're going to take the second 
 selection of  Deploy a virtual machine from an OVF  or an OVA ﬁle  . As I said we have an 
 OVA ﬁle, so that's the selection. Choose the second one and select  Next  . Okay. 
 04:00-05:00 
 We've got to give it a name so we enter a name for the Data Lake VM. In this example, we 
 are going to call it sc-dp, for Stellar Cyber Data Processor Data Lake Master, s c d p d l 
 master, and then we've got to get that OVA ﬁle there. So you've got a choice. You can either 
 drag that OVA ﬁle from wherever it is on your host to that blank space or if you click in that 
 blank space it will open up a dialog box for you to browse to where you can locate that OVA 
 ﬁle. Click Okay and then this is where we'll end up with giving it a name and we can see that 
 our Aella Data Processor. So it's not speciﬁc to a DA or a DL. It's the same ﬁle used for both. 
 And it's the same ﬁle whether it's a master or a worker node or a coordinating node. It's 
 Aella, Data Processor, and then the version number. In this instance it's 4.3.7 and select  Next  . 
 05:00-06:00 
 Right. We're creating our Data Lake virtual machine. Where are we going to put it? We have 
 got to choose one of our datastores. We've previously created these datastores. We created 
 Stellar platform VMs. That's the one with two terabytes of data. Remember the requirement 
 for this virtual machine is 500 gig of disk space. With two terabytes available in that 
 datastore, that's plenty. The only other virtual machine we're going to add to that datastore 
 is the Data Analyzer. Between the two of them it should be one terabyte. We've got double 
 ADM-01-01-224  19 


---

<!-- Página 20 -->

 the space available. The other datastore we can see there is the SC Data Lake storage, and 
 that is used for the Data Lake’s actual storage, not the VM storage. This one's talking about 
 where we're going to put the virtual machine, so we select  Stellar Platform VMs  and choose 
 Next  . Okay. Now it's going to ask what sort of networking  do we have? 
 06:00-07:00 
 Our networking…we can see with that's the networking we previously conﬁgured, Stellar 
 management network. That's our port group previously conﬁgured that was bound to 
 vSwitch0, which is connected to–I can't remember the name of it Vee NIC0. I'm not sure what 
 that was. The network interface is the physical network interface card that will go out and 
 communicate with our other network and security devices. We have to choose how we're 
 going to provision this virtual machine on the disk. What we're choosing between is thin and 
 thick. We choose thick. What this says is that we've told the virtual machine it's going to 
 have 500 gig of disk space and it provisions all of that 500 gig from creation of the machine 
 rather than if we did thin provisioning, it would create the disk space as required, but we 
 want to have a highly e ective and e cient virtual machine, so we will provision it with thick 
 provisioning. 
 07:00-08:00 
 We want to uncheck so that, by default, when you get to this screen it'll have  Power on 
 automatically  checked. We want to uncheck that because  the moment we click  Finish  , it'll 
 go ahead and try and turn on the virtual machine. We have more conﬁguration steps to do, 
 so we don't want it to boot and then have to turn it o  to do that conﬁguration. Uncheck 
 Power on automatically  and select  Next  . We'll be shown  a summary screen of what we've 
 chosen. So we can see we've got a product there: Aella Data Processor. We've got a virtual 
 machine name, the one we made up sc-dp-dl-master, the ﬁle where is it coming from? That 
 came from our OVA ﬁle and which datastores are going to be put in? What sort of 
 provisioning are we going to do? Which network are we going to use? What is the guest OS? 
 If we're all happy there, we select  Finish  to continue. 
 08:00-09:00 
 Once we click  Finish  we can see that the beginning  of the creation of our Data Lake virtual 
 machine. It's in the process of loading that OVA ﬁle and all of the ﬁles within that bundle the 
 ﬁles to create the virtual machine. You can see there it's uploading disk at the moment. It's 13 
 percent run. Depending on where you are uploading this ﬁle from will take a few minutes to 
 maybe ten minutes depending on the speed of whether you're doing it locally or or over an 
 internet connection. Okay. When that's complete, you'll see the next slide. We can see in the 
 next slide we have a created Data Lake. We have a Creative Data Lake virtual machine has 
 been created. But there's a few more steps to do at the moment. If you look, CPUs 16, well 
 ADM-01-01-224  20 


---

<!-- Página 21 -->

 that's not enough for a production network. Memory, that's not enough for a production 
 network. There are a couple of edits we need to do before we continue. 
 09:00-10:00 
 First one: We're going to edit the Data Lake by choosing  Edit  from the menu. We're going to 
 enter the correct CPUs. We're going to add 40 to this selection because we need 40 for a 
 Data Lake virtual machine, and then select  Save  . We  need to edit the Data Lake virtual 
 machine and enter the correct RAM, so that correct is 136 gig. In this example with the 
 checkbox reserve or guest memory, that just means I'm not going to share it if I'm not using 
 it, it's not available to be shared with any other virtual machine. Now on this ESXi host we 
 only have two virtual machines running. We'll have the Data Lake Master and we'll have the 
 Data Analyzer master. There's plenty of memory for each of them. There is no problem with 
 clicking Reserved here. But we should make sure whatever the device is the host is that are 
 running these virtual machines that the memory allocated is enough otherwise it will run 
 into problems if that memory can't be reserved. 
 10:00-10:50 
 We click Reserve and then select  Save  . Alright. To  create the Data Lake virtual machine 
 we're going to validate it one more time. This is like when we were creating the datastores. 
 It's giving us a summary of what we're creating so we look at the CPU, the memory, the disk, 
 we can see here in this example, we've added the summary of the 12 terabytes. We'll show 
 you how to do that in a later lesson and it's ready to be turned on. 
 The lesson,  Virtual Machine Creation Data Lake  , is  complete. You should now be familiar 
 with creating the Data Lake virtual machine. Thank you. 
 L03B-DEMO: Data Lake VM Creation (08m:10s) 
 00:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration 
 module is  Virtual Machine Creation - Data Lake. Virtual  Machine Creation - Data Lake  . This 
 lesson demonstrates the creation of a Data Lake virtual machine in ESXi. The demonstration 
 includes downloading the Stellar Cyber software, creating the virtual machine via an OVA 
 ﬁle, and then changing and checking the CPU memory, network adapter, and hard disk 
 requirements for the virtual machine. 
 Let's start with the software download. If we go to the documentation we can see one of the 
 ﬁrst things to do under the before you begin, we can see step three here is download the 
 Stellar Cyber software. 
 01:00-02:00 
 ADM-01-01-224  21 


---

<!-- Página 22 -->

 To do that we need credentials, and you can get those from Support as it says here contact 
 Stellar Cyber at support at stellascyber.ai for login credentials and a one-time password. Or 
 the license key or an OTP will also see it called. Let's start with this. We'll click on that. It's 
 going to ask us for a username and password that has been given to us from Support. The 
 username and password we enter and then sign in, and we can see here, we are 
 downloading some software one download in progress. Again, if we click on the down arrow 
 we can see our download is that software is coming down. Okay. We can see that that 
 software has downloaded. We're ready to go to our install. 
 02:00-03:00 
 The ﬁrst thing to do is go back to ESXi. Here's our host with zero virtual machines. The ﬁrst 
 thing to do is select  Create / Register  a virtual  machine. We're going to deploy this not by 
 creating a new virtual machine but deploy a virtual machine from an OVF or an OVA ﬁle. 
 You can see that the ﬁle we downloaded was an OVA ﬁle. We select deploy via OVA ﬁle. 
 Select  Next  . We have to give our virtual machine a  name. Let's call it Stellar Cyber Data 
 Lake. I'm going to call it master because at some stage in the future we are going to 
 upgrade our deployment to cluster deployment that may have additional resources. Let's 
 say that this is our Data Lake master. You can either drag and drop a ﬁle here or click to 
 select. 
 03:00-04:00 
 We're going to click to select. We're going to browse for that ﬁle. Here is our ﬁle Data 
 Processor that we just downloaded, and open. Now we have the name of our virtual 
 machine. We have an OVA ﬁle that's going to create the virtual machine and we select  Next  . 
 Okay. It's asking where are we going to store our virtual machine? Well, before we created 
 some data stores, and we said we would create our Data Lake our Data Analyzer virtual 
 machines in a datastore called Stellar Cyber VM, so we'll select that. There is plenty of room. 
 Remember: 500 gigs for each of those virtual machines. We've got a capacity of 1.75. Tiny 
 bits being used which will be just overhead in the conﬁguration of that, so plenty of space. 
 Select  Next  . Alright. Now it wants to know what is  the virtual machine network mapping 
 we're going to use. 
 04:00-05:00 
 Well, that's the latest when we created it. If we look there is the VM network, but we're going 
 to go with the port group that was created in a previous lesson called  Stellar Cyber 
 Management  . We're going to do thick provisioning,  which means it expands the disk on 
 creation rather than creating disk as it's required. We are deﬁnitely  not  going to power on 
 automatically because as soon as this is being created we're going to want to do some 
 edits before we power it on. So with those selections made, select  Next  . Here is a summary 
 of our machine if everything's okay and there's actually not a whole lot to conﬁgure so far 
 ADM-01-01-224  22 


---

<!-- Página 23 -->

 so that summary looks good to me. We click  Finish  . The moment we do that, what we'll see 
 down the bottom here is the creation of our virtual machine. We can see it up here: Our 
 Stellar Cyber Data Lake master. 
 05:00-06:00 
 Down the bottom you can see in the recent tasks is that disk has been uploaded from the 
 ﬁle on this local machine to ESXi. It's creating our ﬁle as we speak. Our disk and our virtual 
 machine so you can see that it's uploading right now, it’s nearly ﬁnished. As soon as that's 
 ﬁnished we'll go ahead and do some edits. Three green ticks so we're ready to continue 
 editing our virtual machine. Now that our virtual machine has been created we need to do 
 some edits. To do that we'll select the virtual machine. Here we are. We can see the defaults. 
 We can see 16 CPUs. That's not enough. We can see memory 64 gig. That's not enough. 500 
 gigs that's ﬁne. Let's go ahead and edit this and make sure that we conﬁgure it correctly. 
 We select  Edit  . Alright. If we go back and remember  from our documentation let's go back. 
 06:00-07:00 
 Our documentation if we look at the requirements, we had the Data Lake is what we're 
 conﬁguring. We need 40 CPUs. We need 136 gigs of RAM and 500 gigs of disk. If we go 
 down the bottom here, because we're doing this in a test environment or a training 
 environment, the minimum you could have is 16 CPUs, 128 gig of RAM and 500 gig. We're 
 going to go with the big deployment. Let's go with forty one thirty six and ﬁve hundred. 
 CPUs we want 40. Scroll down 40, 136 gig, 136 gig, 500 gig of disk, and our network adapter 
 is correct. Right there we could click  Save  , but one  of the things we do actually want to do is 
 ﬁx our memory. 
 07:00-08:10 
 We go down here and we say we want to reserve all of our guest memory. I did that by 
 expanding this little triangle next to the memory and then chose reserve memory. That 
 means that it won't share. It’s always available for our Data Lake virtual machine. Finish that. 
 Click  Save  . Alright. There is our Stellar Cyber Data  Lake Master with 40 virtual CPUs, 136 gig 
 of RAM, 500 gig of hard disk space, and the correct network adapter of Stellar Cyber 
 management. We can see that that's connected, as in it's connected to our virtual switch, 
 which is connected to that physical NIC, which is how we'll get to it, to manage the device. 
 We are ready to power on. 
 The lesson,  Virtual Machine Creation Data Lake  , is  complete. You should now be familiar 
 with creating the Data Lake virtual machine. Thank you. 
 ADM-01-01-224  23 


---

<!-- Página 24 -->

 L04 - DATA LAKE VIRTUAL MACHINE CONFIGURATION 
 L04A-PRES: Data Lake Conﬁguration (16m:05s) 
 00:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module is 
 Stellar Cyber Platform Data Lake Conﬁguration. Stellar Cyber Platform Data Lake Conﬁguration. 
 Okay. We've conﬁgured our Data Lake virtual machine in ESXi. We're just going to start by looking at 
 the summary of that before we power it on and validate it one more time. You might want to check 
 the CPU, check the memory, check the hard disks have been conﬁgured. You can see in this example, 
 there is only one network adapter, and there is only one hard disk. Now for a Data Lake we'll 
 ultimately expect two hard drives, but for this one we just have the one. Let's power it on. We select 
 the virtual machine, and then choose  Power on  . 
 01:00-02:00 
 When you do that just wait a few moments and you will be able to click on the virtual console. That 
 black square that's sitting under console and monitor in this image you can click that and it'll pop 
 open to a window, and that is the console to our virtual machine host. Until we do anything with our 
 IP networking we couldn't SSH to this device from a networking device, we have to do it from this 
 console. Power on the device, wait a couple of moments, and then click on this console. We can 
 watch the machine boot the Data Lake boot the Data Lake virtual machine boot. After it has booted 
 you will be presented with the Data Processor login prompt. There are credentials for that. These are 
 default credentials:  Aella  (a-e-l-l-a) is the login  name and the default password is  change me 
 (c-h-a-n-g-e-m-e). 
 02:00-03:00 
 We will enter  Aella  , and then the password  changeme  .  You can see immediately you are required to 
 change your password immediately root enforcement. We've got to go enter it again. The ﬁrst 
 password to enter is the existing password, that is  change me  , and then followed by your new 
 password and then conﬁrming your new password. Once you've done that, then we'll be left at a 
 prompt ready to conﬁgure this Data Lake virtual machine. The ﬁrst thing we need to do is to give it IP 
 addressing. Now we'll use DHCP by default so we can use the DHCP if there's that on your local 
 network, but if you want to give it some static IP addressing, which is what we're going to do here, 
 we'll go ahead and enter these commands. We can type in a  set interface management IP  , and 
 then give it an address. 
 03:00-04:00 
 In this example our address is 192.168.1.175, and then we've got to give that IP address a mask. In this 
 example it's going to be a /24 or a 255.255.255.0 network mask. Set interface management IP 
 192.168.1.175/24. When you press Enter, you can see there after setting interface IP do reboot and 
 reset to apply the conﬁguration. Yes, we will do that, but we won't do it just yet. We'll just put a couple 
 more IP addressing in: one for the gateway and one for the DNS. You can see those two commands 
 set interface management gateway, and then give it an IP address In this example it is one nine two 
 ADM-01-01-224  24 


---

<!-- Página 25 -->

 one six eight one dot two ﬁve four for a gateway and then a set interface management DNS. We'll 
 give it a DNS of 8.8.8.8 for DNS. 
 04:00-05:00 
 Now the ﬁrst of the show commands we've seen if we do a  show interface  , we can see we have 
 one interface, the management interface and the link is up because it's connected to our port group 
 inside our VM machine, which is connected to our vSwitch0, which is connected to that physical NIC 
 that's connected to an external switch. We have a link of up And an IP address we can see there of 
 that 192.168.1.175 with our mask written with a 255.255.255.0 or a /24. It's all good there. Everything 
 looks ﬁne. Once we've done that, we can SSH to the box and you can see here from Mac in this 
 example it's SSH, and then the username Aella (a-e-l-l-a) @ and the address we just gave at the 
 192.168.1.175. We will have to conﬁrm our ﬁngerprint with a  yes  . 
 05:00-06:00 
 You can see at the bottom of this page, we have that same prompt that we had in our console. Now 
 the reason for using SSH over that virtual console is we need to have a bit more control of what we 
 can do in an SSH host depending on what client you're using, the console in ESXi is not very forgiving. 
 For example, if you typed in  show ?  , it will run up  the screen and there's no way to scroll up. Where if 
 we had a good SSH client, we can scroll up and see more of what's available in our show's question 
 mark. There you go. Log in with Aella, use the new password that you created in that last section 
 during the boot. Alright. Just to conﬁrm,  show interface  There it is again: 192.168.1.175 with a /24 bit 
 mask and  show gateway  gives us the information we  want:  192.168.1.254. 
 06:00-07:00 
 All good there for our interface and our gateway. The last one to check is our DNS conﬁguration. We 
 do a  show DNS  to show 8.8.8.8, which is what we conﬁgured.  So the test there with a shell dig plus 
 short meaning it's just shortening the output of what's been returned of www.Google.com and we can 
 see a bunch of responses there. We actually know that the conﬁguration is working correctly. I show 
 a host name. We'll just  show Data Processor  . We actually  want to give it a host name. When we 
 go into the UI we will see this host name listed when we look at the Data Lake.  Set hostname 
 sc-dp-dl-master  is code for Stellar Cyber, DP, Data  Lake. Sorry. Stellar Cyber, Data Processor, 
 Data Lake, master. It's any host name you'd like to give it. 
 07:00-08:00 
 Again, it's asking you to reboot and then reset. At this stage that's what we're doing. From within our 
 SSH client we will issue the  reboot  command and you  can see it's closed that session. The device, 
 the virtual machine will now be rebooting. If we go back to the console, because it's the only place we 
 can watch it, we can't SSH to a device that's booting, but we can watch from the virtual console within 
 ESXi we can watch it boot. That screenshot is just an example of some of the messaging while it's 
 booting up. We've received our login prompt and we can SSH back into our device with the username 
 and the host IP address of that 192.168.1.175. There we are. 
 08:00-09:00 
 ADM-01-01-224  25 


---

<!-- Página 26 -->

 With our new password, not  changeme  , the new password. Conﬁrming that we are back into our Data 
 Lake. We've booted the box, we've changed the IP addressing, and now we're ready to conﬁgure a 
 little further. Now we need to set it a role. Our device, our virtual machine is a Data Lake, but it's not 
 really known as a Data Lake at the moment. All it was was a host with a host name. The  set role 
 command and you can see the available roles at the top. AIO is for an all in one. We can create a 
 Data Processor that's got a Data Processor and a Data Lake all in one, not for production networks. 
 These are for test networks. Makes the deployment a little bit easier. Resource is we'll see resource 
 used when we create the Data Analyzer because you can see in that in that list of availability there's 
 no DA, no Data Analyzers so we create it as a resource ﬁrst and then in the UI create the resource 
 into a Data Analyzer. 
 09:00-10:00 
 You can see there what we want to choose is  DL-master  .  A  set role DL-master  , and we can see 
 there that now in the screenshot below it's pretty important. When you do this if you do it too quickly 
 after booting, you can see in that screenshot of the  set role DL-master  , it comes back and says 
 CLI service is still initializing. Please wait and try again. Just wait a few moments and you can actually 
 press the up arrow and then enter and it'll issue the same command again. It's just waiting for that 
 CLI service to boot. Right. Now we have this as part of a cluster. It's not an all in one, so we need to 
 give it a cluster name. A  set cluster_name  , and then  name the cluster. In this example, the cluster's 
 going to be called  sc-dl-cluster  . This is the Data  Lakes cluster that we're conﬁguring here and a 
 show cluster_name  … 
 10:00-11:00 
 …  will show that that command was successful. Well,  the  Set Cluster Name Success  was the 
 giveaway that it was successful, but just to test a  show cluster underscore name  will give us the 
 name of that cluster. We can see there  sc-dl-cluster  .  We have to give the cluster a size. The 
 command for that is  set cluster_size  and it's a cluster  size of one. When we do a  show 
 cluster size  just to conﬁrm, again we're just conﬁrming  if we looked at the output from the set 
 cluster size one, we can see set cluster size success, but just to conﬁrm  show cluster_size  and 
 we can see the output of that command is one. At the start you can see there set the size of the Data 
 Lake cluster. Well, at the start of this there's only one. There is a Data Lake master and then we'll 
 increase it by one each time we add a worker node. We'll use a  set cluster_size  and a  show 
 cluster_size  to see that. 
 11:00-12:00 
 A  show interface  . There is no di erence here. We're  still just conﬁrming our 192.168.1.175. The 
 reason that's important is we're going to do a  set  cm  , which is the conﬁguration manager. A  set cm 
 for this deployment will be using the IP address of the Data Lake Master’s Management IP. A  show 
 interface  gives us that output of 192.168.1.175. A  set cm  of 192.168.1.175 is the command we need. 
 To conﬁrm that, we do a  show cm  we can see there  the output 192.168.1.175 has worked. We have set 
 the conﬁguration manager correctly. Right. The ﬁnal thing to do is to set an OTP because after we've 
 conﬁgured this… 
 12:00-13:00 
 ADM-01-01-224  26 


---

<!-- Página 27 -->

 …this virtual machine will go and pull images from Stellar Cyber repository of data to create this 
 virtual machine. Now without a licensed OTP or a one-time password, our license without a valid one 
 of those, it won't pull down all of the images. We need to do a  set otp  and then type in our OTP 
 that we received via email from Stellar Cyber as part of the deployment. That example 
 there–a123b432c123–is a made up one. It's just an example, so please don't type that in. It will not 
 work for you. Once we do a  set OTP  and then we can  do a  show otp  and we can see that it's been 
 veriﬁed successfully. Again, the a123 is just a mock number so please don't use that. It will not work. 
 13:00-14:00 
 Right. Now we have typed in We've entered the conﬁguration for the IP addressing. We've set up the 
 clustering. We've given it a host name. We have rebooted the box and now it's time to do a reset. 
 With the conﬁguration commands of the Data Lake in the CLI complete, it's time for a rese. We issue 
 a command  reset  to conﬁrm that because it's going  to go and reset all of our pods or all the 
 services running and start pulling down new images. It asks us for a conﬁrmation with a capital YES. 
 So it says, “Are you sure? Type upper case YES,” and then o  it goes. It will start resetting the device. 
 To see where it is up to, we use the  show status  command.  What we're looking for here is you can 
 see how many pods are running and it tells you how many it's expecting to see. 
 14:00-15:00 
 In this case at the very beginning there are zero pods running, and it's expecting at least 39 to be 
 running. The image is installed on host. Depending on what type of deployment that is and what 
 images are required, you will see that 33. That number will get up well into the eighties and 
 sometimes I've seen into the early nineties. There are images that have been pulled down from a 
 Stellar Cyber server to pull those images down and then to get those pods up and running. It can 
 take ﬁve, ten, ﬁfteen minutes depending on loads and depending on your network activity. Continue 
 to do a  show status  . We've got a couple more screenshots  that will show us that. Here is another 
 show status  and we can see now we have some pods running.  In this output we can see we have 17 
 pods running, still not even halfway of how many we're expecting to see. 
 15:00-16:05 
 There are 59 images, still not near the high eighties or early nineties we're expecting, so continue to 
 be patient while those images come down and those pods start running. Let's look at another one. 
 We are ﬁnished! All pods are running. 90 images are installed on this host, and the big green “system 
 ready,” that's what we're looking for. That's great news. Everything's come down. Now clearly our OTP 
 is working, and you can see there the OTP was veriﬁed. Again, that's just a mock OTP address but 
 you'd see your real one there a system ready. That's it. That's the Data Lake conﬁgured up until this 
 stage from a CLI perspective. The next thing we'll need to do is to jump into the user interface, the 
 web pages of our Stellar Cyber platform, and do some more conﬁguration in there. 
 The lesson,  Stellar Cyber Platform Data Lake Conﬁguration  ,  is complete. Thank you. 
 L04B-DEMO: Data Lake Conﬁguration (17m:10s) 
 00:00-01:00 
 ADM-01-01-224  27 


---

<!-- Página 28 -->

 The next lesson in the  Stellar Cyber Open XDR Platform Installation and Conﬁguration 
 module is  Stellar Cyber Platform Data Lake Conﬁguration.  Stellar Cyber Platform Data Lake 
 Conﬁguration  . Demonstration of the initial console  CLI conﬁguration for the Data Lake. 
 In this demonstration I will show you the conﬁguration steps of the Data Lake console 
 including the initial login to the console requiring a password change, the networking 
 conﬁguration settings and validation, setting hosts and cluster names, role and 
 conﬁguration manager settings, and of course then the resetting and watching it come up 
 all ready. Let's start with powering on the Data Lake virtual machine. Alright. Here is our ESXi 
 host. 
 01:00-02:00 
 We'll go check our virtual machine. There it is, our Stellar Cyber Data Lake master. We can 
 either check the box here and choose  Power on  , or  you can select the virtual machine and 
 click  Power on  from here. Let's do it from here because  I want us then to open up this 
 console to watch the machine boot. Let's do that power on. We can see down here the 
 recent task is Power On virtual machine, successfully completed. We click on this. We'll get a 
 console. Let's now watch the Data Lake boot. Just about ﬁnished. The change in font is a bit 
 of a giveaway. Here we are. We have a login prompt. Alright. The username is  aella  , 
 a-e-l-l-a. 
 02:00-03:00 
 The ﬁrst password, the default password is  changeme  .  All lowercase and no spaces, 
 c-h-a-n-g-e-m-e. We're then asked to immediately change the password. We entered 
 changeme  again. That's the current password,  changeme  .  I'm going to enter a new 
 password and conﬁrm the new password. Here we are in the DP. Alright. The ﬁrst thing to 
 do, let's set some IP addressing because if we do a  show interface  we can see we have 
 an IP address, but this is a DHCP IP address and I don't want that. I actually want to set an IP 
 address. Let's start with  set interface  tab, space  m-a-n  , tab, IP… 
 03:00-04:00 
 …and the address we're going to give it is 192.168.1.234 and we'll give it a mask a  /24  bit 
 mask  Enter  . Now it does say here to reboot and reset,  which we will do. We're just going to 
 put a couple more conﬁguration settings in. We could do a  show interface  to see that 
 our new IP address of the .234 has been set. We're now going to give it a gateway and some 
 DNS information.  Set interface  tab,  m-a-n  tab to complete  that command,  gateway 
 tab, the gateway IP address is  192.168.1.254  .  Enter  .  We could do a  show gateway 
 command to show that the gateway conﬁguration has been set. We'll do a  set 
 interface… 
 ADM-01-01-224  28 


---

<!-- Página 29 -->

 04:00-05:00 
 …  Management dns  to a  8.8.8.8. Enter  .  Show DNS  . Okay.  We've got all those now. Okay. 
 Now that we've got a conﬁguration on there I want to SSH the box so that we can have a 
 better console rather than this virtual console within ESXi so I'm going to close that down 
 and open up a SSH. Okay. Here's my PuTTY, which I'm going to use for SSH. I'm going to 
 load up a proﬁle that I've conﬁgured earlier, and (select)  Open  . Okay. The ﬁrst time I'm 
 going to use it here we need to accept the ﬁngerprint, so accept. So  aella  to log in and our 
 new password, not  changeme  ,  but our new one. 
 05:00-06:00 
 Here we are. Have we got the right device  show interface  ?  Yes we do. We can see there 
 that we've got 192.168.1.234.  Show gateway  . Yes we've  got gateway,  show dns  . Yes. We've 
 got the correct DNS. The ﬁrst tests we can do here is let's ping. We need to do an  !ping  . 
 Let's ping our gateway  192.168.1.254  . Great. We can  do that. Let's ping our DNS.  !ping 
 8.8.8.8  . This will check that our gateway is working.  We can ping our disk. The last one to 
 check that our DNS settings are correct. Let's do a  shell dig  to  google.com  , and we 
 can see that is also working because we've got an answer there of that 142.251.46.206. 
 06:00-07:00 
 Okay. They are all set correctly. The next thing is to set the hostname, reboot it, log in, and 
 then set some role information, so standby why we do this. We do a  show hostname  . It's 
 just what we've got. Let's  set hostname  to be  sc-dp-  (for Data Processor)  dl  (for Data 
 Lake), and it's going to be the  master  .  Enter  . Okay.  You can see there it says to reboot and 
 reset, which we will do. We will do that. Well, let's do that right now. We've lost our party 
 session. We'll close that. Let's go and look at our ESXi console to watch it boot. 
 07:00-08:00 
 We'll see as soon as this font changes. There we go. Now we can log in. We'll be able to 
 open up our party session again. Let me do that.  aella  ,  the new password, and here we 
 are. Okay. A  show hostname  . We can see that we've  now got our new host name. Fantastic. 
 Alright. The next thing to do is to set the role. We're going to do a  set role  . If I enter we 
 should get a list of what's available. We're going to set ALs up as a DLmaster.  Set role 
 DL-master  . Okay. We have it now set as a DL master.  The next thing we need to do 
 because this is not an all in one is we need to set the clusters up. We're going to give this a 
 cluster name. That gives us the ability to have multiple Data Lake nodes run into that. They 
 run in a cluster. Let's set that up with a  set cluster_name  tab. Yep. Let's say cluster 
 name. We're going to give this a Stellar Cyber dash Data Lake cluster (  sc-dl-cluster  ). 
 That's our name. Set successful, and we're going to do a  show cluster_name  . See that 
 was set correctly. Now we need to give the cluster size.  Set cluster  this time at size not 
 ADM-01-01-224  29 


---

<!-- Página 30 -->

 name (  set cluster_size  ). We're going to give cluster size and one because at this stage 
 we only have one node being this DL master running in this cluster. It's that size of one. We 
 can do a  show cluster_size  to conﬁrm that worked.  There we are at one. 
 09:00-10:00 
 Okay. The next thing we need to do is set the cm, the conﬁguration manager. To do that 
 we're going to set it to the same IP address as our Data Lake master. If we do a  show 
 interface  we can see that's our address, our 192.168.1.234.  We're going to do a  set cm  to 
 192.168.1.234  . Fantastic. A  show cm  . Fantastic. That's  been set correctly. Now we need to 
 set our license because after this it's going to go pull packages down from the Stellar Cyber 
 site. Now without a licensed version of this, it won't pull all of the packages down. Now we 
 do that with a  set OTP  command. You can get that in  your welcome pack that you'll 
 receive or from Customer Support. Don't use this one. We're going to cover this up. This is 
 our training OTP, so it won't be useful to you… 
 10:00-11:00 
 …but let me go ahead and set that command now. Okay. There's our  set otp  . You can then 
 do a  show otp  , and it will show you what you've got  that has been successfully veriﬁed. 
 The last thing now to do is to do a reset and watch the packages come down. Let me do 
 that now. We do a  reset  . It says caution. Yes. We  do want to do a reset. We have to answer 
 with as it says down the bottom type uppercase  YES  ,  so Y-E-S in uppercase.  Enter  . Now it's 
 going to go ahead and start pulling down images and starting to run the pods. The way we 
 can verify what's going on with this when we get a command prompt back is to do a  show 
 status  . I'll walk you through the process of how to  do that. It takes a little bit of time while 
 all of the packages or the images are pulled down. 
 11:00-12:00 
 If we do a  show status  . Okay. We can see there what  we're looking at or want to highlight 
 your attention to is zero pods running and it has an expectation of at least 39. We can see 
 that there are 27 images installed on the host. That number will increase. We can see there 
 in red there are microservice images missing. They are being pulled down right now. A lot of 
 red there that's going on, so I will continue to run a  show status  . What we want to see is 
 that the pods running is increasing and the images installed is increasing. I can just press up 
 arrow for  show status  again.  Enter  . Alright. We still  have zero pods running, but we now 
 have 30 images installed. We can see that the images are coming down. Okay. 
 12:00-13:00 
 We could see up here it was 27 images, and now it's 30 images, but still zero pods. We'll try 
 that again. Up arrow  show status  . What have we got  now? Thirty-two, so still no pods 
 running. We'll keep an eye on that and 32 images installed on the host. I will stop talking. 
 ADM-01-01-224  30 


---

<!-- Página 31 -->

 There's not much for me to say, but I will continue to press up arrow to bring back the 
 command  show status  or you could just type it in.  But we'll speed up this part of the video 
 so we don't have to wait and watch for the entire pods to be running. I'll stop every once in a 
 while and chime in of what I'm seeing and what I'd like to draw your attention to until we 
 have it complete. Stand by. Alright. There is something to mention here. We can see in the 
 last version of  show status  that we now have six pods  running, so that has started to 
 increase. 
 13:00-14:00 
 We can also see from the last version of this that the 34 images installed on the host has 
 increased to 37 images. I believe it gets in excess of 80 images. It depends on what sort of 
 deployment it is and whether it's a DA or a DL, but it gets I think maybe even into the 90s for 
 images. They're coming down right now as we're waiting and watching, but we do want to 
 see the pods running increase and the images installed on the host to also increase. Let me 
 just check one more time while I'm talking to you.  Show status.  We were six and 37. 
 We're now eight and 40. I will pause while we wait for these to come down and spin up. 
 Okay. What can we see here? We are up to 26 of at least 39 of the pods running and 66 
 images installed. 
 14:00-15:00 
 It is progressing as planned. I do keep checking it occasionally. I've witnessed that these 
 stall. If that's the case, you just do another  reset  and it goes as a clean up and pulls down. 
 It actually doesn't remove what it's already brought down, but it does reset all the pods. If it 
 does stall, that's something that you can do is just to do another  reset  . But do keep an eye 
 on it and make sure that the images are coming down and the number of pods running is 
 increasing. Let's do another  show status  . Let’s see  where we're up to. Thirty-six of 39. The 
 number of pods is very close. Eighty-six images on the host. That is also very close, so not 
 too long now and we will have our Data Lake up and running. 
 15:00-16:00 
 Now although I didn't mean to do a  show interface  before, it's probably quite telling for 
 us to see those RX bytes is at 19 gig that shows all these packages that are coming down all 
 these images as it says here these 86 images installed on host, they'll come in through this 
 management interface in the RX byte. I'm going to actually do that again. Let's do a  show 
 interface  . We can see that it is growing. Just in  the last time I did that it's gone from 19.6 
 to 20.3. Let's do a  show status  and see where we're  up to. Okay. Thirty-six and 89. We 
 have three more images and still the same amount of pods running. We're getting very 
 close, but we're not there yet. Standby. What we can see now is 89 images have been 
 installed on host. All images and below that you can see all images to run microservices are 
 ready. 
 ADM-01-01-224  31 


---

<!-- Página 32 -->

 16:00-17:10 
 All images to support platform are ready. While we're waiting on now is those 36 pods 
 running to be as it says at least 39. Standby. We're very close now. Okay.  We can see that 
 we now have all 89 images are installed in the host. All pods are running. That's been the 
 change from 36 to 37 to 38. Now we have all pods are running. Just the last couple of things 
 that it's cleaning up around the manifest ﬁle. We’re nearly there. As you can see now all 
 pods are running. All images are installed on the host and the most important is what's there 
 in green writing System Ready. We are ready to sign into the UI. 
 The lesson,  Stellar Cyber Platform Data Lake Conﬁguration  ,  is complete. Thank you. 
 L05 - DATA ANALYZER VIRTUAL MACHINE CREATION 
 L05A-PRES: Data Analyzer VM Creation (08m:50s) 
 00:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module is 
 Virtual Machine Creation - Data Analyzer. Virtual Machine Creation - Data Analyzer  . Just looking at 
 the minimum requirements for the DA the Data Analyzer we can see in the circled area, the Data 
 Analyzer requires 44 CPU or vCPU, virtual CPUs, 64 gig of RAM so a little less than the Data Lake and 
 the same 500 gig for the actual virtual machine itself. That's on the ESXi device. To go ﬁnd those 
 minimum requirements, please go to the documentation and you will ﬁnd this is just a screenshot of 
 what's available in those documentations in the Knowledge Base. 
 01:00-02:00 
 The minimum requirements for a demo environment or training environment, you can see we've 
 dropped the DA CPU from 44 down to 16. RAM remains the same 64 gig and of course the disk space 
 in the virtual machine in ESXi remains at 500 gig. We will have plenty of space for that. You can see 
 the DA and the DL virtual machines will be stored in the same datastore. If there is su cient room on 
 our datastore, you can put the Data Lake there as well for a demo or for a training environment. In a 
 production environment, Data Lake needs to be in its own datastore for performance. To create this 
 Data Analyzer, this virtual machine, we'll navigate to virtual machines on the left side and then select 
 the  Create / Register VM  to create it. You can see  we've already created the SC DP DL-Master. 
 02:00-03:00 
 Now we're going to create the SC DP DA-master. Navigate to  Virtual Machines  , click on  Create / 
 Register VM  . We're going to use the same ﬁle that  we downloaded and used for the Data Lake, the 
 same ﬁle to create the Data Analyzer. We'll use the OVA. Select the middle one:  Deploy a virtual 
 machine from an OVA or an OVA ﬁle  . We’ll be using  an OVA ﬁle, so it's that middle selection, and 
 then click  Next  . Enter the name for your DA virtual  machine in this example. Of course you can name 
 it whatever you like. Our example is SC DP DA (for Data Analyzer) dash master (SC DP DA-Master). 
 ADM-01-01-224  32 


---

<!-- Página 33 -->

 This will be the ﬁrst one in a scalable environment. We're only going to create one, but if we were to 
 have many this will be the master virtual machine. We can of course have worker nodes… 
 03:00-04:00 
 …DA worker nodes to add to this to increase the scalability of this Data Processor. We give it a name, 
 and then we either drag the ﬁle into that open space, it starts o  as being blue open space, or if you 
 click in that space, it'll pop up a menu where you can browse to ﬁnd that ﬁle. We're looking for that 
 aella Data Processor 4.3.7. Remember, we’re doing 4.3.7 so in a later lesson we can upgrade it to 5.1.1 
 and show you how that process works. When you've done that, select  Next  . Okay. Now where is it 
 going to be stored? This is choosing the datastore of where your virtual machine will be placed. 
 We've created two datastores: the SC Data Lake storage, that's where we're going to put our Data 
 Lake, but where we're going to put our actual virtual machines is in the Stellar platform VM. We select 
 Stellar Platform VMs  and choose  Next  . 
 04:00-05:00 
 Okay. Networking, we will go choose a network connection for the virtual machine the DA at this in 
 this deployment in our basic deployment we'll only have one network interface. We're selecting the 
 Stellar management network in this example. For disk provisioning, we choose thick, which makes the 
 space available at the creation of the virtual machine, and then we uncheck our  Power on 
 automatically  because there's some changes there's  some edits we want to make prior to turning on 
 the machine. Make sure you uncheck that if you forget and you turn and we've clicked  Finish  , all it's 
 going to happen is it's going to boot straight away and we'll have to power it down so we can do 
 these edits before turning it on again. Easy here just to uncheck the default because it is checked by 
 default. Uncheck the  Power on automatically  so that  we can make these edits. When you've done 
 those changes, select  Next  . 
 05:00-06:00 
 You'll now see a window that shows you your summary of your virtual machine that's about to be 
 created. You can see the product is aella Data Processor. It is a VM. That's the name we gave it. Make 
 sure that the datastore is correct and your provisioning is thick as we said, and the right network 
 conﬁguration. If it's not, you click the back button and go and ﬁx that, else if it's all ready to go, only 
 thing left to do is select  Finish  . Now once you click  Finish  you can see down the bottom of your ESXi 
 webpage, you'll see that the progress and at the moment it is uploading that OVA ﬁle from wherever 
 it was that it was stored to your virtual machine to that datastore. That's where it's been created. Just 
 wait a few moments depending on where it comes from, if it's a slow network connection it might 
 take a little bit longer, but it takes a couple of minutes and it will upload that virtual machine. 
 06:00-07:00 
 We can see now that the virtual machine has been created. There it is. You can see that little green 
 dot for the SC DP Data Lake or DL master. That means it's on and running our SC DP DA master. It 
 does not have the little green icon. It has not been turned on yet, but it's ready to turn on except we're 
 going to make a couple more edits prior to turning it on. We're going to select the SC DP DA Master 
 and make some more edits. Once you've selected it, this is the screen you'll be presented with. At the 
 top there on that menu bar there is an Edit button so we select the  Edit  button. You can see here 
 ADM-01-01-224  33 


---

<!-- Página 34 -->

 we're going to change the CPUs. This will be a production environment example so a minimum of 44 
 CPU, virtual CPUs. You can see there is a reservation of those CPUs. Now this is up to you of what 
 your deployment looks like. 
 07:00-08:00 
 In our example here, there is one ESXi box that's hosting only the two VMs, one VM for the Data Lake 
 master and one VM for the Data Analyzer master. In that scenario, it’s not necessary to reserve the 
 CPU as they'll be shared between the two Stellar Cyber virtual machines. But if you have a larger 
 environment where your virtual machines, your DA DL Stellar Cyber virtual machines, are on a shared 
 environment with other servers, other virtual machines, then it would be wise to reserve the CPU so 
 they're always available to these virtual machines. You would check that reservation and then click 
 Save  . Okay. Another edit for the virtual machine is  to reserve the memory. Again same thing as the 
 CPU. 
 08:00-08:50 
 I would defer to say yes, reserve it. It's probably a good habit to get into to make sure that when 
 these devices spin up that they've got their CPU and memory available to do all of the functions that 
 are required. When you ﬁnish that, click  Save  . At  the end of it we'll be given back our summary and 
 you can see there that the CPU is correct, check that the memory is right, the hard disk is correct, and 
 the network adapter is right. Once that's all conﬁrmed, your virtual machine is ready to be powered 
 on. 
 The lesson,  Virtual Machine Creation Data Analyzer  ,  is complete. You should now be familiar with 
 creating the Data Analyzer virtual machine in ESXi. Thank you. 
 L05B-DEMO: Data Analyzer VM Creation (08m:50s) 
 00:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module…is 
 Virtual Machine Creation - Data Analyzer. Virtual Machine Creation - Data Analyzer  . Demonstration of 
 the creation of the Data Analyzer virtual machine in ESXi. 
 In this demonstration, I will show you the creation of the Data Analyzer virtual machine in ESXi, 
 including the system requirements. We'll have a look at the documentation again. We've already 
 downloaded the Stellar Cyber software when creating the Data Lake, so we don't need to download 
 that again. We'll go through creating the VM via the OVA ﬁle that we just talked about downloading, 
 and we will change and check the CPU memory and network adapters for the virtual machine. 
 01:00-02:00 
 Let's get started with the requirements of the Data Analyzer virtual machine. Here we are in our 
 Knowledge Base. Just to navigate there rather than searching we could search or navigate. Let's 
 navigate. We're  INSTALLING | Installing a Data Processor  | Installing a Data Processor in VMware 
 as a cluster  . You could do the same thing. Let's do  it. Let's do it. If I go back to home, if I type in 
 VMware cluster  in the search, let's see what shows  up. There we are, I  nstalling a Data Processor in 
 ADM-01-01-224  34 


---

<!-- Página 35 -->

 a VMware Cluster  . Just so you know, up at the top it gives you a UI: Installing | Installing Data 
 Processor | Installing a Data Processor in VMware (Cluster). That's the same way we've been 
 navigating. Either one works. It will then also highlight. You can see any of the words that we had put 
 into the search. I'm just going to remove that from the URL… 
 02:00-03:00 
 …so we don't have those words. Okay. Before we begin some system requirements. We're talking 
 about the DA this time, the Data Analyzer. So over here in this column we can see the host needs 44 
 88 cores because we're going to have 44 for the Data Analyzer, RAM 64 gig, OS for the VM 500 gig 
 that's what we're going to make sure of. Then down below from a minimum perspective, and we 
 could lean towards the minimum being that this is a demonstration / training deployment, 16 CPU 
 rather than the 44, we still need the 64 gig of RAM, and we still need the 500 gig of space. Let's go 
 ahead and install that. Okay So here we are in our ESXi host. If we select Virtual Machines, We can 
 see that we have a Stellar Cyber Data Lake master but we're going to create a Stellar Cyber Data 
 Analyzer master. Select  Create  . 
 03:00-04:00 
 We're going to do it from an OVA ﬁle. Choose the middle selection and  Next  . Give it a name: Stellar 
 Cyber Data Analyzer Master. We need to select that OVA ﬁle. I'm going to browse by clicking there. 
 I'm going to select the Data Processor OVA ﬁle. Select  Open  . Now we have that ready to go. Select 
 Next  . Where would we like to store this? We're going  to store it in the same place as we stored the 
 Data Lake Master, that is in the datastore Stellar Cyber virtual machines or VMs. Select  Next  . Alright. 
 Which VM Network are we going to use–that port group? We can see we've got two to choose from. 
 We're choosing the one we created earlier Stellar Cyber management, and we're going to thick 
 provision, which means it provisions the disk space rather than expanding as required. 
 04:00-05:00 
 We are not going to turn it on automatically because we want to edit before we go further. Select 
 Next  . Alright. Here's a summary. In case you've made  some mistakes, you can always click back to 
 go and ﬁx those. We have an aella Data Processor. The name of it is Stellar Cyber Data Analyzer 
 master. You can see it's pulled this information, which has come from that OVA ﬁle. The datastore is 
 on the Stellar Cyber VM. It's thick provisioning. It's going to use the Stellar Cyber management 
 network for networking. Its guest OS is in Ubuntu Linux. That's it. Let's click  Finish  . Down at the  bottom 
 under  Recent Tasks  we’ll see that it's created the  VM and it's starting to upload those disks. Let's let 
 that complete. Okay. Nearly there. 
 05:00-06:05 
 We now have our Stellar Cyber Data Analyzer master. We've got to make some edits to this before 
 we go and make sure we've conﬁgured it correctly. Let's go in here and we've selected it. We're going 
 to choose  Edit  to edit the virtual machine. We were  going to give it 44 cores. Let's give it 44. Sixty-four 
 was the memory, 500 was the disk. It's got the correct network adapter. We click  Save  . All done. All 
 there's left to do now is power it on. 
 ADM-01-01-224  35 


---

<!-- Página 36 -->

 The lesson,  Virtual Machine Creation Data Analyzer  , is complete. You should now be familiar with 
 creating the Data Analyzer virtual machine in ESXi. Thank you. 
 L06 - DATA ANALYZER VIRTUAL MACHINE CONFIGURATION 
 L06A-PRES: Data Analyzer Conﬁguration (08m:25s) 
 00:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module is 
 Stellar Cyber Platform - Data Analyzer Conﬁguration. Stellar Cyber Platform - Data Analyzer 
 Conﬁguration. 
 Now that our virtual machine has been created in ESXi, it's ready to power on. Just one last time 
 before you power it on, check that you've got the CPU correct, the memory correct, the data storage 
 is the 500 gig on the right datastore. Networking is correct. If all that's good to go, we're ready to 
 power on. After you've selected the VM, the virtual machine, from this  Virtual Machines  tab on the 
 left, then choose the  Power on  button at the top.  Now while it's powering on you can see that in the 
 virtual console. 
 01:00-02:00 
 We're unable to SSH to this device remotely because of course it doesn't have any IP addressing, so 
 we can only use the virtual console to see what's going on. At that stage, once it's complete in the 
 boot, we’ll be presented with this screen where we log in for the ﬁrst time. The ﬁrst time we log in at 
 the login prompt we enter the following default credentials:  aella  (a-e-l-l-a) is the default login 
 name, and then the default password is  changeme  (c-h-a-n-g-m-e).  Type that in  aella  and 
 changeme  . The very ﬁrst thing you're required to  do, as it says on the screen, you're immediately 
 asked to change that default password. The steps are you enter the default password again. That's 
 the current password of  changeme  (c-h-a-n-g-e-m-e)  all lowercase. Then enter your new password 
 and conﬁrm it. Once that's done you'll be presented with your prompt in your CLI, ready to make the 
 conﬁguration changes. 
 02:00-03:00 
 The conﬁguration changes: We have got to give it some IP addressing. It will use DHCP by default, so 
 the actual host will receive an IP address if you have a DHCP server on that network segment. We're 
 going to use static IP addressing. The commands required for that is a  set interface 
 management IP  , and then the IP address and the netmask.  In this example we can use a /24 for a 
 24-bit mask. You can see in the output there it translates our /24 into a 255.255.255.0 in the octet 
 notation. We've done a  set interface management IP  192.168.1.150  . As we saw before, our 
 Data Lake is .175, so they're on the same network, the /24 network. The next thing to do is give it a 
 gateway. 
 03:00-04:00 
 ADM-01-01-224  36 


---

<!-- Página 37 -->

 A  set interface management gateway  is the command. In our example, 192.168.1.254 is the 
 gateway. The ﬁnal command here for our IP addressing is a  set interface management dns  , 
 and then the DNS address In this example, it is 8.8.8.8. Then a  show command  or  show interface  . 
 Show int  is enough. If you actually type in  show int  and press tab, it will extrapolate and expand 
 that syntax out so it will actually end up being  show  interface  . We can see in the  show 
 interface  command that our IP addressing is correct  of the 192.168.1.150. You can see in the output 
 straight after we enter that IP address it asked us to do a reboot and a reset. You don't have to do 
 that immediately, but it is required before we continue too far. To add then the gateway address and 
 the DNS settings is just ﬁne to do those three… 
 04:00-05:00 
 …IP set interface commands before we continue. Alright. Some show commands, a show interface. 
 We can see that IP address in there a show gateway command will show us the gateway of the .254, 
 which we conﬁgured before, and the  show dns  of 8.8.8.8.  Now there's a couple of commands you 
 can use to test that these have worked step by step. I mean the ﬁrst one I would do would be a pin to 
 the gateway. You can see down at the bottom it's a  shell ping 8.8.8.8  . The other way to do it is 
 !ping  and then the gateway address. In this example  192.168.1.254 to make sure that we can get at 
 least to our gateway that would prove our IP addressing is correct. The next step would be to ping as 
 it says there shell ping 8.8.8.8 to ping something beyond our default gateway. 
 05:00-06:00 
 Again,  !ping 8.8.8.8  . Make sure that our default gateway  conﬁguration is working. The ﬁnal one 
 to test whether the DNS conﬁguration is working, is to do a  shell dig www.google.com  . That will 
 show us that our DNS is resolving. They're the three commands we can use, or four commands we 
 can use to make sure that our IP addressing is correct. Once that's done we can SSH to the device. 
 We know it's now working. We can SSH to aella. That is our login name, at 192.168.1.150. First of all 
 you'll have to conﬁrm the ﬁngerprint with a yes and then you're presented with the login prompt. Now 
 the login name is aella of course, but the password is no longer changeme; it's whatever you've 
 changed it to during that very ﬁrst login where you're forced to make a password change. Right. 
 Show host name  . 
 06:00-07:00 
 We do a  show host name Data Processor  not terribly  helpful to us when we get into the UI and 
 want to identify this virtual machine. We'll do a  set host name  then. The host name we're choosing 
 is  sc-dp-da-master  , or if I'm to expand that would  stand for Stellar Cyber Data Processor, Data 
 Analyzer, and it's the master one of those. Again, you see it asks you to do a reboot and a reset. At 
 this stage after entering our IP address in and conﬁrming that it's correct, adding a host name it's 
 now time to reboot. Hit the reboot and you'll see immediately your connection via your SSH client has 
 been closed. We'd have to go back to the ESXi virtual console to watch the device boot up again. We 
 didn't watch that boot up again. We're just assuming it booted up. Here we are. We have SSH back 
 into the box and now we're going to set a role. Previously with the Data Lake we set it a role of Data 
 Lake Master. 
 07:00-08:00 
 ADM-01-01-224  37 


---

<!-- Página 38 -->

 When we conﬁgure a Data Analyzer, we start by just setting its role to a resource. We can see there 
 with the ﬁrst command  set role resource  . The  show  role  command will show that that stuck. 
 We've got the resource as our role. We set the cm. The CM or the conﬁguration manager is the IP, the 
 management IP address of the Data Lake. That's the virtual machine we created four which had the 
 example of 192.168.1.175.  Set cm  to the management  IP address of the Data Lake interface, and a 
 show cm  will show that we've done the correct settings  there. Now we need to do a reset. The reset 
 will ask us to conﬁrm with a capital YES, an uppercase Y-E-S to start resetting our pods and pulling 
 down whatever software is required. 
 08:00-08:25 
 Now at this stage it's not a DA, it's just a resource. It will pull down the required images that are 
 needed just for a resource. At this stage we can go and watch what's going on. 
 The lesson,  Stellar Cyber Platform Data Analyzer Conﬁguration  ,  is complete. Thank you. 
 L06B-DEMO: Data Analyzer Conﬁguration (09m:15s) 
 00:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module is 
 Stellar Cyber Platform - Data Analyzer Conﬁguration. Stellar Cyber Platform - Data Analyzer 
 Conﬁguration  , Demonstration of the initial console  CLI conﬁguration for the Data Analyzer. 
 In this demonstration, I will show you the conﬁguration steps in the Data Analyzer console including 
 the initial login to the console requiring a password change, the network conﬁguration settings and 
 validation of those settings, setting up the host and cluster names, and setting a role and 
 conﬁguration manager settings, and of course resetting the virtual machine. Let's start with powering 
 on the Data Lake virtual machine. Here we are in ESXi. If we go to our virtual machines we can see 
 we've got two. 
 01:00-02:00 
 We've got this one powered on our Stellar Cyber Data Lake Master. That's that little green play icon 
 we can see just above there. We can see that our Stellar Cyber Data Analyzer master is not yet 
 powered on. We're going to select it, and we're going to select  Power on  . Wait just a couple of 
 moments and then we will open up this console to watch it boot. Here we go. There's our prompt. 
 Same as with the conﬁguration of the Data Lake, the Data Analyzer, it's aella. The password, the 
 default password, which will change immediately, is change me c-h-a-n-g-e-m-e. Here we are 
 immediately being asked to change that password. We've got to type in the current password, which 
 is change me c-h-a-n-g-e-m-e. 
 02:00-03:00 
 Now it's asking for our new password to enter. Conﬁrm that new password. Fantastic. Here we are in 
 our console of our Data Analyzer master. The ﬁrst thing to do, set some IP addressing. Okay. We start 
 with  set interface  m-a-n  management, IP, and the address  with a mask  /24  bit mask for that 
 network and  Enter  . It does say here to reboot and  to reset, both of which we will do after we put in 
 ADM-01-01-224  38 


---

<!-- Página 39 -->

 just a few pieces of conﬁguration here. The ﬁrst one is to set the gateway: set int, tab management 
 tab… 
 03:00-04:00 
 …gateway space. The gateway is 192.168.1.254 (  set  interface management gateway 
 192.168.1.254  ). Now we've got our gateway. Again,  it's asking us to do that reboot and reset, 
 which we will do at the end. We've got to set up some DNS settings, so  set interface  . Look if I just 
 type in two letters and press tab, nothing happens. I need that third one to make it unique. Interface 
 management DNS, 8.8.8.8. Enter. Okay. Fantastic. We've got enough conﬁguration items here that we 
 can SSH to this device now. Let me go ahead and do that. One moment. Okay. Here we are with a 
 PuTTY session or an SSH session to 192.168.1.233. 
 04:00-05:00 
 It asks us to accept the ﬁngerprint, accept, and we're going to log in. We're going to log in as aella. 
 Our new password, not  changeme  , but our new password  (types). Here we are in our Data Analyzer 
 console. Okay. A couple more things to do now. Let's just check where we are. We'll do a  show 
 interface  . We can see we are on 192.168.1.233. That  is the one we're expecting to see. Let's do a 
 show gateway  . That is correct, .254 is the gateway.  A  show dns  will show us the 8.8.8.8, which is 
 correct. Let's test those now. Let's see if we can ping our gateway. So  !ping  192.168.1.254  . We 
 always want to check that the networking is working correctly before we continue. 
 05:00-06:00 
 We can ping our gateway is working. Let's ping our DNS server to prove that the routing is working. 
 !ping 8 .8 .8 .8.  That is working. The ﬁnal one to  test is to do a shell dig to google.com to 
 conﬁrm that our DNS is working (  shell dig google.com  ).  We can see that's working there with 
 our responsive or the answer of 142.250.189.238. Okay. They're all working now. Now let's give it a host 
 name. What have we got right now? If we do a  show  hostname  it is just Data Processor. Let's give it 
 a host name.  Set hostname  . I did a tab then. Stellar  Cyber-data processor-Data Analyzer-master 
 (  sc-dp-da-master  ). Let's use the same convention we  used for the Data Lake. 
 06:00-07:00 
 If we do a  show host  let's see what that says. See  it's still there. This is where we need to do a reset 
 to conﬁrm that that's going to work. At this stage, let's do a  reboot  , r-e-b-o-o-t. Our SSH session will 
 be discontinued, but we'll go look at the virtual console in ESXi to conﬁrm where it's up to. We'll move 
 that out of the way. Let's have a look. We can see here we are rebooting. Okay. We could log in there, 
 but let's go back to our PuTTY session and run it again. Restart session. Okay. There's our login at the 
 bottom. Type  aella  and our new password. Okay. Here  we are. 
 07:00-08:00 
 Alright. We are in our Data Processor. If we do a  show hostname  now, that's what we expect to see. 
 That's the name that's going to show up in the UI that  sc-dp-da-master  , That's why we're sort of 
 interested in that because we want to see what it is up there. Okay. Now we need to set the role for 
 this. If we do a  set role  , we can see there that none  of those options are for a DA. In this example 
 what we will do is set it up as a resource and then inside the UI, the user interface is where we 
 ADM-01-01-224  39 


---

<!-- Página 40 -->

 conﬁgure it as a Data Analyzer. The command for this is  set role  . I could actually just press up 
 arrow here to bring back the last command,  set role  resource  . Okay. That looks like we've got it. 
 It's in that prompt now but let's do a  show role  . 
 08:00-09:15 
 The role is of a resource. So fantastic. Alright. We need to do a  set cm  .  Set cm  to 192.168.1.234. We 
 want to set the cm to be the management interface of the Data Lake. That's the other IP address. 
 This device as you can see up here is .233. Alright. That is our cm. We'll do a  show cm  . What did I do? 
 What did I do wrong? I typed in the wrong address. I typed in 268, not 168. Of course 268 is outside 
 the range of available addresses.  Show cm  . There.  Okay. That's fantastic. We are ready for a reset 
 with a big fat capital  YES  , Y-E-S, to allow that to  happen. Okay. That's going to take a while while 
 that's going on. We'll come back. 
 The lesson,  Stellar Cyber Platform - Data Analyzer  Conﬁguration  , is complete. Thank you. 
 L07 - DATA PROCESSOR CONFIGURATION 
 L07A-PRES: Data Processor Conﬁguration (09m:50s) 
 00:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module is 
 Stellar Cyber Platform - Data Processor Conﬁguration. Stellar Cyber Platform - Data Processor 
 Conﬁguration  . 
 This is the ﬁrst time we're actually going to log in to the user interface of our DP, our Data Processor. 
 Data Processor is  made up of a Data Lake and a Data Analyzer. In our example we've got a Data 
 Lake master and a Data Analyzer master, that Data Analyzer master has not yet been conﬁgured. It 
 is currently just a VM as a resource. In this module we'll show you how to convert that from a 
 resource to a Data Analyzer. The ﬁrst thing to do is to use your browser and browse to the Data Lake 
 management IP in our example, that 192.168.1.175. 
 01:00-02:00 
 We use admin. It's not aella in the UI. It is admin with a password of changeme. Add admin to the ﬁeld 
 and select  Next  . For the password, the very ﬁrst  time it is changeme. You won't see it written like that. 
 We've put it there just to make it really clear for you but it's changeme (c-h-a-n-g-e-m-e) all 
 lowercase. Then select  Sign In  . The ﬁrst thing you'll  have to do is update your account by entering 
 your email address for the admin account so put an email address in there, a conﬁrmation email 
 address and then select the  Change Email  button. The  next thing to do we'll have to change the 
 password for the very ﬁrst time. Your existing password is changeme (c-h-a-n-g-e-m-e) and then 
 enter your new password making sure that it matches all the requirements of how many characters… 
 02:00-03:00 
 ADM-01-01-224  40 


---

<!-- Página 41 -->

 …how many uppercase and lowercase, numbers, special characters, make sure you get a bunch of 
 green ticks, and then conﬁrm that password and select  Change Password  . You'll immediately be 
 logged out of the UI. To log in with your new credentials. You can either use admin or your email. 
 Either one of those will work and select  Next  . This  will be your new password that you just created. 
 Once you've done that, select  Sign in  . You'll be presented  with the Stellar Cyber end user license 
 agreement, the EULA, of which you can have a read. If you're happy with it, select  Accept  to move on. 
 You'll then be presented with the default homepage of the Stellar Cyber UI. This is actually one of the 
 visualization dashboards to select, but this is the default homepage that we'll be looking at. 
 03:00-04:00 
 The ﬁrst thing to do is to convert our resource to a Data Analyzer. The ﬁrst thing we need to do from 
 the menu is select  System  . From the grouping  Data  Processor  , select  Resources  . In this page you will 
 see the resources that are conﬁgured in this Data Processor. After navigating to  System | Data 
 Processor | Resource  page, this is what we presented  with. We can see our Data Lake has already 
 been conﬁgured and is one of the resources in this page. The other resource we're seeing is the one 
 that we gave the host name sc-dp-da-master is available. I want you to pay particular attention to 
 the available column and the tick meaning that resource is available for us to turn into a Data 
 Analyzer. As the note says, do not edit the resource directly in the  Data | Data Processor | Resources 
 page, this page. 
 04:00-05:00 
 Instead, we're going to use the  System | Data Processor  | Data Analyzer  and we're going to create a 
 Data Analyzer utilizing this resource. Navigate to  System  under the  Data Processor  column and 
 choose  Data Analyzer  to get to the Data Analyzer creation  page. Once at this page there is a  Create 
 button. You can see in this screenshot there is no Data Analyzer created yet. We'll have to create one 
 from the resource. We already know it's going to be the Data Analyzer. That's that virtual machine 
 that we've created earlier. We open that Data Analyzer page and select the  Create  button. The 
 pop-up menu we'll be presented with is to create our Data Analyzer. Now the example here, the name 
 sc-dp-da-master, is exactly the same as what we call the resource. 
 05:00-06:00 
 Probably better o  calling this sc-dp-da-cluster would be a better example of which the DA Master 
 will be. The resource will be one of the devices in this cluster, the cluster of Data Analyzers. In our 
 example, we are only going to have one Data Analyzer, just the master. We won't have any worker 
 nodes in there. But a better example to call it the cluster rather than call the host the master and the 
 cluster the master. That's really what we're asking here. We can see the cluster name is chosen from 
 our Data Analyzer name. Ports are conﬁgured, but we haven't added a role yet. We haven't added a 
 resource to that. We can see there under  Cluster Nodes  that we have an  Add Node  button. That's 
 what we will choose next. Choose  Add Node  and then  from those drop-down menus, we can see 
 there is our Data Analyzer, our sc-dp-da-master. That's just the name of the host. 
 06:00-07:00 
 Remember we did a  set hostname  . This is where that  shows up when we did that from the 
 command line on our virtual machine. Then we have to give it a role if within this cluster. The ﬁrst role 
 ADM-01-01-224  41 


---

<!-- Página 42 -->

 we have to have is a DA master. From that drop down, we choose  DA master  . When we've done all 
 that, select  Submit  . We can see there, wait a few  minutes as it says wait a few minutes to refresh the 
 Data Analyzer conﬁguration page because it has to go create that. While we're waiting there is a little 
 recircle button just to the left of the search and we can just tap on that to refresh this screen. Once 
 it's done, we want to make sure that the node list in the column. We've gone from zero nodes to one 
 node. We chose a node in that last conﬁguration screen. We also want to see that the status has a 
 green dot in that column and that we're ready to go. 
 07:00-08:00 
 If you click on the  node  button, it will display all  of the nodes within the Data Analyzer cluster. Within 
 that Data Analyzer cluster, we have a host named sc-dp-da-master. That is our virtual machine that 
 was created earlier in ESXi. We can see there, free disk space, plenty of disk There's the 484 which is 
 around the era of the 500 gig we gave it in ESXi. It’s all looking good there. Finally we just want to 
 conﬁrm a few other things. We've created our Data Lake virtual machine and conﬁgured that We've 
 now created a resource that we've turned into a Data Analyzer. We just now want to make sure that 
 there's a couple of bindings that have been conﬁgured correctly. The ﬁrst one is to check that there's 
 a default receiver. You can see there check default receiver conﬁguration because Stellar Cyber 
 automatically conﬁgures this, a default receiver… 
 08:00-09:00 
 …to be used as a destination of data collector, sensors, and other data sources. Before you add data 
 sensors, to your new DP or new cluster, check the conﬁguration of your default receiver. To do that 
 we go to  System  . Under the  Collection  category, click  the  Receivers  button to see what receivers 
 we've got. There we go. We can see that there is a default receiver. Now the other piece to make sure 
 or to conﬁrm is that the receiver host name is set to the IP address of the DA Master, it’s not set to 
 the IP address of the Data Lake Master. Just conﬁrm that conﬁguration. In our example, the dl master 
 was 192.168.1.175. We do not want to see that here. What we do want to see is the DA Master IP 
 address of 192.168.1.150 or whatever it is for your IP addressing. 
 09:00-09:50 
 Final to check that our default sensor proﬁles are using the default receiver. Again, select  System  , 
 and then from the  Collections  category, select  Sensor  Proﬁles  . We can see there we have two 
 default sensor proﬁles: default and default modular. One is a standard proﬁle type. The other is a 
 modular sensor proﬁle type. But what we want to see in that Receiver column is that they're using the 
 default_receiver that was created by default. Just a conﬁrmation. 
 The lesson,  Stellar Cyber Platform - Data Processor  Conﬁguration  , is complete. Thank you. 
 L07B-DEMO: Data Processor Conﬁguration (07m:30s) 
 00:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module is 
 Stellar Cyber Platform - Data Processor Conﬁguration. Stellar Cyber Platform - Data Processor 
 ADM-01-01-224  42 


---

<!-- Página 43 -->

 Conﬁguration  . This lesson demonstrates the completion of the setup steps in the Stellar Cyber user 
 interface. 
 In this demonstration, I will show you the conﬁguration steps in the user interface, or the UI, including 
 initial login to the UI requiring our password change, acceptance of the EULA (end user license 
 agreement), and adding an email address. We're going to conﬁrm the resource availability to create 
 the Data Analyzer. Then we're going to create the Data Analyzer master. Then we're going to check 
 on some default conﬁguration. We're going to check on the receiver conﬁguration. 
 01:00-02:00 
 We'll also then look to make sure that the sensor proﬁles have that receiver conﬁguration in there 
 too. Let's start with signing into the UI for the ﬁrst time. Okay. We're going to start with admin, not 
 root, admin.  Next  . changeme. Here we are again c-h-a-n-g-e-m-e.  I need to update my email 
 address.  Change Email  . Now we need to give it the  original password, which was c-h-a-n-g-e-m-e 
 (changeme) and put in our new password. Right. The fact that that came up, the button came up to 
 change password means that they match. We've got all these ﬁve green ticks saying that I've 
 matched the password requirements, change password. Alright. 
 02:00-03:00 
 Out we go again. Back in here. You can either use the username, which is admin, or you can use the 
 email address that you just entered. I'm going to use admin because it's a bit quicker. Okay. This time 
 we're asked to accept the end user license agreement. Have a read of that agreement. When you're 
 done, select  Accept  . Here is the default home page.  What we now need to go and do is conﬁrm the 
 resource availability.  System | Resources  and we can  see a resource available. We have the host 
 sc-dp-da-master. That's the host name we gave it in the CLI, in the console. We can see the tick there 
 that says Available, so that's great news. 
 03:00-04:00 
 We have a resource available to turn into the DA Master. Okay. What we're going to do is  System | 
 Data Analyzer  . We can see we do not have a Data Analyzer  right here, so we need to create one. 
 Create  . I'm going to give it a name of Stellar Cyber-dp-da-master.  That's what we're going to call it. 
 The cluster name; it gets the cluster name from the Data Analyzer name. We can't change the ports 
 you can see and we need to do something else in here. We need to add a node to this. We will click 
 Add node  . The resource where we saw we had one available.  That's our host. We're familiar with that 
 233 IP address. It is not a DA-worker. It will be a DA-master because we need to have at least one 
 master of course. Once that's done we select  SUBMIT  . 
 04:00-05:00 
 Now at ﬁrst you'd wonder well, what happened? It says it was successful. Data Analyzer was added 
 successfully in that green bar, but I don't see anything here. There is a button up here, the refresh 
 button, that we can wait. We just have to wait a few moments for that to be created. So standby. 
 Okay. We hit the refresh button. Nothing yet. No DA conﬁguration yet. Let's standby. Let's go back 
 and have a look at the  Resource  page while we're doing  that to see what's happened over there 
 System | Resources.  We can see that the resource is  no longer available and the status is green. But 
 ADM-01-01-224  43 


---

<!-- Página 44 -->

 when we go to  System | Data Analyzer  we can see we have nothing. There it is! It just appeared. It 
 just appeared in the table. What I was going to do is go back to the console, the SSH session and 
 show you what it looks like in there. Let's have a look in here. We can see it's now DR Master. 
 05:00-06:00 
 If we do a  show status  it's also downloading some  pods. We are waiting for that. Now if we 
 jumped over here maybe a little earlier, we would have seen that this was in a much earlier 
 conﬁguration and that's why it was not showing in our list. Let's wait for these all to get up and 
 running before we go look further. What we could do in here…let's do this. We can see here in the 
 node list that we have our sc-dp-data master. That's great. Thank you for the DA. That's what we 
 want to see in there, but we're just going to wait for all of our pods to come up and running. There we 
 go. Okay. We can see that we have the system ready. Let's go back to our UI. Alright. Here we are in 
 our UI. We went in here before. 
 06:00-07:00 
 We see we do have a node in our node list, which is fantastic for our Data Analyzer conﬁguration. But 
 we want to also check that our default receiver and our Modular Sensor has that default receiver. Go 
 to  System | Receivers.  We can see we have a default  receiver. Let's go and have a look inside that 
 receiver and conﬁrm that the address is the Data Analyzer, not the Data Lake. Now when we look at 
 that I would say that is the Data Lake’s IP address, not the Data Analyzer. We want to change that to 
 233 to conﬁrm that that's going to work. That's where the data is going to be received to, so click 
 SUBMIT  . The other thing we want to check is we want  to go into our Modular Sensors. Sorry, not the 
 Modular Sensors, the sensor proﬁles. They'll be two created by default: default and default modular. 
 07:00-07:30 
 One is a standard sensor and one is for Modular Sensors. We just want to go and look at those and 
 make sure they've got that receiver conﬁgured and we can see it here actually in the column 
 Receivers:  default_receiver. We can see in both of  those. Everything looks good. We're ready to 
 proceed. 
 The lesson,  Stellar Cyber Platform - Data Processor  Conﬁguration  , is complete. Thank you. 
 L08 - DATA LAKE ADDITIONAL DRIVE CONFIGURATION 
 L08A-PRES: Data Lake Additional Drive Conﬁguration (07m:55s) 
 00:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module is  Data 
 Lake - Data Lake Additional Drive. Data Lake - Data Lake Additional Drive  . 
 What we've got here is a login to the Data Lake virtual machine CLI or the console. We've logged in 
 with our aella and our password, and we've done a  show storage  command. What we can see in 
 the result of the  show storage  is that device named  SDA one of 499.9 gig. That's our 500-gig drive 
 ADM-01-01-224  44 


---

<!-- Página 45 -->

 that was created when we made the virtual machine earlier. Just a 500-gig drive. Now we did create 
 a datastore with more than 12 terabytes of data storage. 
 01:00-02:00 
 We would expect to see that in here, but at this stage the virtual machine has not had that added. 
 Before here's a  show storage  ,  which shows that that  does not exist. There is no signiﬁcant sized 
 drive there. No two plus terabyte in a test or a training environment. Or in a production environment 
 there is no 12 plus terabyte storage. Let's go ahead and create that. In ESXi from the left panel under 
 Virtual Machines  , select our Data Lake virtual machine,  our sc-dp-dl-master, and we're going to edit 
 that virtual machine to add the additional disk. We navigate there. We select our virtual machine and 
 from the menu above, select the  Edit  button. From  the pop-up window we can see what we've 
 already got in our virtual machine and what we need to do is add that second hard drive for the Data 
 Lake. The datastore there is the Data Lake and create a space on there. 
 02:00-03:00 
 From above under the  Virtual Hardware  tab, we're going  to select  Add Hard Disk  . Now we're going 
 to add a standard hard disk to our virtual machine. From this pop-up window we can see our original 
 hard drive of 500-gig and now our second hard drive that we're adding. The ﬁrst thing we need to do 
 is change the location to the datastore where we're going to store the Data Lake. We created that 
 datastore earlier, the SC Data Lake Storage. That's the datastore that was created in ESXi where we 
 kept adding the drives to get it to a total of more than 12 terabytes of disk space. The ﬁrst thing to do 
 is to browse to that area and choose that datastore. Once that's done we can then increase the size 
 of our hard drive. Once you've done that… 
 03:00-04:00 
 …click up the top there and we can increase that, as you can see, to 12 terabytes. You have to make 
 sure that there's at least 12 terabytes available to do that. In our datastore we do have that correct. 
 Once we've browsed to the right datastore, set the disk space to the desired amount. As we said, for 
 a production network, 12 plus terabytes of data storage in a training or a demo environment, at least 
 two terabytes of Data Lake storage. Once that's been conﬁgured correctly, choose the  Save  button. 
 A bit of a summary of what our hardware looks like. Our vCPUs of 40 for our Data Lake, 136-gig of 
 RAM. The ﬁrst hard drive, the 500-gig of storage is where our virtual machine is being stored. That's 
 that use and we can see our hard disk too of now 12 terabytes that we're going to use for our Data 
 Lake storage. 
 04:00-05:00 
 What this does is add the virtual machine. It adds the hard drive to the virtual machine, but there's 
 more conﬁguration steps required to change our Data Lake that is currently using the 500-gig, 
 clearly not enough to use our 12 terabytes. From hard disk one to hard disk two we'll see what those 
 changes look like. Now from the CLI, we can see or in the console the CLI, we can see that with a 
 show storage  command, there is now an sdb device name  with 12T to 12 terabytes of disk storage. 
 Fantastic! The virtual machine knows that now we added that second drive. We can see our two 
 drives there. sda1 of 500-gig or 499.9. That's where our VM is stored and our operating system and 
 our software. For the Data Lake we're going to add it to sdb, the 12 terabytes of storage. 
 ADM-01-01-224  45 


---

<!-- Página 46 -->

 05:00-06:00 
 The way we do that is with the  add storage blk  command.  Add storage BLK  , and then the 
 name of the device. We saw in the previous slide the device name was sdb, so add  storage BLK 
 SDB  . Once we enter that command we can see that add  the storage will erase and format the 
 selected disks. Make sure that we've selected the correct disks. We most deﬁnitely have. Conﬁrm with 
 an uppercase or a capital Y. We're looking for the result of success. Right. Now we can see that we've 
 got mount point for our extra storage, our 12 terabytes of storage. Note that 
 /opt/stellar/es-data-lvm. We're going to see that name when we go into the UI to migrate from the 
 existing 499.9-gig drive or the 500-gig drive… 
 06:00-07:00 
 …which has been used for our virtual machine, our software and we will migrate that to our new data 
 storage for our Data Lake, that 12 terabytes. Take note of that name and we'll see that again when 
 we jump into the UI. From within the UI we're going to navigate to  System  and then to  Data 
 Management  . Under  Data Management  , select the tab  Advanced  . From the  Advanced  tab is where 
 we're going to do this migration. We can see there we need to migrate from the existing datastore. 
 Where B is highlighted, there is a drop down and we will see in that drop down our new storage, our 
 /es-data-lvm. We're going to migrate from /esdata to /es-data-lvm that was attached to. 
 07:00-07:55 
 That's the mount point for our 12-terabyte hard drive. Once you've done that, select  Start Migration  . 
 Now that the migration is done, let's go into our Data Lake and conﬁrm that we now have that mount 
 point correct, and we have 12 terabytes of storage. Go to  System  , then under the  Data Processor 
 grouping, select  Data Lake  . Next to the node list,  select that and we'll get our pop up. What we're 
 looking for under our data storage is 12 terabytes. If we recall before, it was that 500-gigabytes of 
 data storage. Now we're over 12 terabytes or 12,000 gigabytes. That's correct. That's what we're 
 expecting to see. 
 The lesson,  Data Lake - Data Lake Additional Drive,  is complete. Thank you. 
 L08B-DEMO: Data Lake Additional Drive Conﬁguration (11m:25s) 
 00:00-01:00 
 The next lesson in the  Stellar Cyber Open XDR Platform  Installation and Conﬁguration  module is  Data 
 Lake - Data Lake Additional Drive. Data Lake - Data Lake Additional Drive  . This lesson includes a 
 demonstration of adding a datastore for the Data Lake to the Data Lake virtual machine and the 
 migration of data to this new large storage directory. 
 In this demonstration I will show you the conﬁguration steps in ESXi, the Data Lake console, and the 
 Data Processor's user interface to add the Data Lake storage to the Data Lake virtual machine. The 
 steps will include conﬁrmation of the datastore, and we'll look at that both in, actually we'll conﬁrm 
 what we ﬁrst see in the UI, then we'll have a look at the datastore and conﬁrm its existence in ESXi. 
 ADM-01-01-224  46 


---

<!-- Página 47 -->

 01:00-02:00 
 We'll validate the current storage in the Data Lake via the console. We'll add a second drive to the 
 Data Lake virtual machine, migrate the Data Lake storage to the new drive or the new directory, and 
 validate the additional storage and the migration was successful. Let's start with the conﬁrmation of 
 where we are right now. First of all, let's log into our user interface, admin. Okay. Here is our user. No 
 data of course because we haven't conﬁgured anything. There's no Modular Sensors. There are no 
 log forwarders. There are no connectors there. There's nothing coming into the system at the 
 moment, so it's going to be pretty fresh. We can go to  System  and we're going to look at the Data 
 Lake. This is the Data Lake we expect to see. You can just grab these columns to make them wider. 
 The name is our Stellar Cyber Data Lake, our cluster. 
 02:00-03:00 
 Now, the column we're interested in is this node list. Let's make that wider so we can see it. We've got 
 our node list right here. It's a button that we can click on. It's going to show us what is the nodes that 
 are in our cluster. Our cluster is Stellar Cyber DL cluster (sc-dl-cluster). Inside our cluster we've got 
 Stellar Cyber dp-dl-master (sc-dp-dl-master) in the cluster. What we're interested in here is data 
 storage. How much data storage have we got? 484 gigabytes. Well, that's using the 500-gig that 
 came with the virtual machine. We created that datastore that Stellar Cyber VMs datastore for the 
 virtual machines, not for the Data Lake. We know we created another datastore for that. So let's go 
 over to ESXi and see what's in there. We can see at the moment of our Data Lake Master we have 
 one hard drive of 500 gig. That's it. That's where if we connected up connectors and sensors… 
 03:00-04:00 
 …log forwarders, that's where the data will be in this side there's 500 gig and that's not what we want. 
 We know we had to have a minimum of two terabytes for our demo or training system but in a 
 production system, 12+ terabytes of data. Let's just jump into our console and have a look at what it 
 thinks. Alright. This is aella. Okay. Here we are.  Show storage  . We can see in here what we're seeing 
 is that 499.9 gig, that's where it is currently storing. It's not where we want it to go. Let's have a look 
 about adding some storage. Let's close our console. Let's conﬁrm our datastores. We select  Storage  . 
 04:00-05:00 
 It's this one we're after–the Stellar Cyber Data Lake. 5.24 gig is certainly more than the two required 
 for a test or a training system, but certainly not enough for a system which has a minimum of 12 gig 
 for that. Okay. We've got that datastore and that's where we want to choose the drive to be, that 
 we're going to add to our virtual machine. Back to  Virtual Machines  , back to our Data Lake, and 
 select the Data Lake. We can see here we have one hard drive here of that 500 gig that matched up 
 with the show storage we saw in the console. Let's edit. We're going to (select) the  Virtual Hardware 
 tab. We're going to add a hard disk. It's going to be a standard hard disk. We can see immediately 
 we've got a hard disk one: 500 gig. There we go. Now if we look where this one is, this one is stored in 
 our Stellar Cyber Data Lake Master, Stellar Data Lake Data Lake. Okay. Great. 
 05:00-06:00 
 ADM-01-01-224  47 


---

<!-- Página 48 -->

 If we look where this one is stored and browse. We want to make sure. Let me just expand this so you 
 can see them all. Here are our datastores. We don't want to use the VMs because we know that's only 
 one disk of one point seven gig but we want the big datastore the Stellar Cyber Data Lake. Okay. And 
 select. Now we know that Data Lake was ﬁve point something gig. Why don't we just make this ﬁve? 
 Five terabytes is how big that storage will be and we want it thick provisioned. Okay. We're going to 
 select  Save  . Doing some work down the bottom here.  Reconﬁguring our VM. Complete successful. 
 Now we can see we have hard disk one is 500 gig. Hard disk two is ﬁve terabytes. Let's go back to 
 our console and conﬁrm what we've got now with a  show storage  . 
 06:00-07:00 
 Okay. Now we can see we have an extra disk in here. We can see that we've got that sdb of 5T, ﬁve 
 terabytes that didn't exist there before. But that's not enough. We need to do a little bit more. We 
 need to add this storage. The way we do that is an  add storage blk sdb  and  Enter  . Add the 
 storage we'll erase and format the selected disks. Yep. We know that's going to happen. So we need a 
 capital Y to continue. It's got a bit of work to do here. Success! That's what we want to see. Let's do a 
 show storage  again. Now what we can see here is… 
 07:00-08:00 
 …we've got our Stellar Cyber Elasticsearch data storage, ﬁve terabytes. Take note of that 
 /opt/stellar/es-data-lvm. We're going to see that when we go into our UI. That's the next thing we're 
 going to do now that we've conﬁrmed that. Okay. Back to the UI. We want to see this data storage 
 space go from 484 to ﬁve terabytes. At the moment 484 gigabytes, we want to see ﬁve terabytes or 
 5,000 gigabytes. Let's do that. Okay. Let's go to  System  and  Data Management  . Under the 
 Advanced  tab, we'll see the current database directory  is /esdata, but if we select this drop down, 
 we'll see now is that new mount point that we saw in the  show storage  command in the CLI. 
 08:00-09:00 
 Start migration. It's going to migrate our Data Lake storage from /esdata to /es-data LVM. Select 
 Start Migration  . Okay. Let's log back in. Let me just  jump over here and see what's happening. We 
 can see as part of that migration that it's reset the services or the pods on our Data Lake master on 
 our VM machine. If we do a  show status  we can see  we've got nine pods running. We're expecting 
 39. It's not ready to log into just yet. Let's keep checking when we see our green system ready is what 
 we're looking for. We can see we've climbed from eight pods running to 20. 
 09:00-10:00 
 Let's wait until we have the system ready before we jump back into the UI. Okay. All pods are up and 
 running. We're just in for the Data Lake cluster to be ready. Standby. Alright. Here we go. System 
 ready. Let's go back to our UI and sign in. When I've come back to the UI like this and there's no 
 Stellar Cyber logo here, I know that it wasn't ready for us to sign in. There weren't some pods that 
 had come up and running so I'm going to refresh this browser. That looks better. Let's now log in. 
 Admin. Here we are back in our user interface. Let's go and check how our migration went, not just 
 our migration… 
 10:00-11:00 
 ADM-01-01-224  48 


---

<!-- Página 49 -->

 …but the addition of the disk to the virtual machine and then the conversion of our space to use that 
 disk and then our migration from the 500-gig disk to the ﬁve-terabyte disk. Let's have a look at what 
 we can see in here.  System | Data Lake  . Our Data Lake  cluster is happy. Let's go check out the node 
 list. We can see in the node list we have data storage space of 5,079 gigabytes, which is our 
 ﬁve-terabyte drive. Our system, our Data Processor, made up of a Data Lake and a Data Analyzer, 
 both clustered, are ready for nodes to be added if we expand and scale this system. It is ready for 
 use. 
 11:00-11:25 
 The next thing to do would be to add connectors, add sensors whether they're Modular Sensors, 
 server sensors, Windows and Linux, it's ready to go. 
 The lesson,  Data Lake - Data Lake Additional Drive  demonstration  , is complete. Thank you. 
 L09 - RECONFIGURING THE DATA PROCESSOR FOR CLUSTER 
 ARCHITECTURE 
 L09B-DEMO: Extended Content Reconﬁguring the Data Processor 
 (33m:00s) 
 00:00-01:00 
 Reconﬁguring the Data Processor  is an extended content  lesson in the  Stellar Cyber Open XDR 
 Platform Installation and Conﬁguration  module. The  extended content lesson,  Reconﬁguring the Data 
 Processor,  includes a demonstration of how to reconﬁgure  the Data Processor from a basic 
 deployment architecture to a cluster deployment architecture. 
 In this demonstration, I'm going to show you the conﬁguration steps in ESXi and the Stellar UI and the 
 Stellar CLI on how to reconﬁgure the Data Processor from a basic deployment architecture to a 
 cluster deployment architecture. The steps are going to include, like the big picture of the networking 
 change, I'm going to show you the existing setup and we'll see that in both the UI, the CLI, and in ESXi. 
 01:00-02:00 
 We're going to shut down the Data Lake and the Data Analyzer virtual machines. We're going to add 
 networking in ESXi. We'll be adding virtual switches and port groups, then we're going to add that 
 networking conﬁguration to the virtual machines–the Data Lake and the Data Analyzer–then we're 
 going to make some console changes in the CLI to the Data Lake and the Data Analyzer around 
 clustering. Okay. So let's start with the big picture of the networking change. We can see here this is 
 what we've conﬁgured so far. We have a Data Analyzer and a Data Lake. They're both masters: a 
 Data Lake master, a Data Analyzer master. They are conﬁgured in ESXi from a networking 
 perspective to communicate with vSwitch0 through a common port group. 
 02:00-03:00 
 ADM-01-01-224  49 


---

<!-- Página 50 -->

 In this diagram the port group's called VM Network. I think we used a di erent port group in the lab. 
 We'll have a look at what that is in a moment. Now what I want to show you is in this example this is 
 the basic network architecture from a cluster network perspective. What that means is the 
 communication that occurs between the Data Lake and the Data Analyzer occurs in the same 
 vSwitch that communication to manage the Data Processor is the same vSwitch that information 
 coming from the network, from our security devices and our networking devices comes in how log 
 forwarding our network tra c, our connectors, APIs, all come in through that same virtual switch. 
 We're going to have a look at a di erent way of doing that and that will be by adding a cluster or 
 another vSwitch to it. Here's the addition. You can see here now we have this vSwitch cluster… 
 03:00-04:00 
 …down the bottom of that diagram with its own port groups. Now for the moment, let's just focus on 
 the Data Analyzer and the Data Lake. They now have grown from having one network interface to 
 two network interfaces, though that second network interface will be connected to this vSwitch 
 cluster. Of course to connect to a virtual switch you have to go through a port group so we'll add a 
 port group for the Data Lake and the Data Analyzer to communicate with that vSwitch cluster. Now in 
 this diagram, there is a physical NIC card that is bound to that vSwitch cluster that is vmnic1. The 
 purpose of that would be if you were to scale this deployment and have worker nodes and those 
 workers being Data Analyzer workers or Data Lake workers and you had them on a separate 
 physical ESXi box… 
 04:00-05:00 
 …you would have that connected to that cluster switch. Two physical hosts running a hypervisor, in 
 this case it's running ESXi, and they need to be able to communicate. Those worker nodes need to be 
 able to communicate with the masters. Whether they're coordinating nodes or networking nodes, 
 they must be able to communicate. That's the reason for that external cluster switch connecting via 
 vmnic1 to our virtual switch to be able to connect into our Data Lake and our Data Analyzer both of 
 those being the masters in this conﬁguration. Let's go have a look at what this looks like in ESXi, but 
 we'll start in the UI and see what that looks like. Okay. Here we are in our UI. Let's have a look at what 
 our system has. Okay. Probably not a lot going on here. Let's do it just a quick  Investigate | Threat 
 Hunting  . 
 05:00-06:00 
 Turn on all of our indices to see that we do have tra c coming in. We are set to a time interval of the 
 last 15 minutes. We can see in the last 15 minutes, yes, there has been some tra c coming in: Syslog 
 tra c, Modular Sensor tra c, and our VMware is coming in as some Syslog tra c, but been 
 identiﬁed via a parser port of course. Alright. We do have information coming in. Let's look at the 
 conﬁguration settings of our Data Lake and our Data Analyzer. We'll start by going to  System | Data 
 Lake  . Alright. We have a Data Lake. We'll just expand  this column. We have a Data Lake 
 conﬁguration of sc-dl-cluster. If we look at the node list to say, “How many nodes do we have 
 participating in that cluster?” We can look and we can see we have sc-dp-dl-master. 
 06:00-07:00 
 ADM-01-01-224  50 


---

<!-- Página 51 -->

 That device is 192.168.1.234. Do pay attention to that address when we come back in and have a look 
 later. One DL master, which has a node of one node in there at the moment. Let's have a look at the 
 Data Analyzer.  System | Data Analyzer  , and we can  see here our sc-dp-da-master if we go into our 
 node list here's our .233. Do pay attention to this address in 192.168.1.233. We look at our node list and 
 there is that actual host in there 192.168.1.233. I don’t want you to pay attention to that because if we 
 go back to our conﬁguration here, this is what it currently looks like. We've got our DA Master, and the 
 DL master, the Data Lake and the Data Analyzer masters, all sitting on the same network. That is the 
 192.168.1.0/24 network. 
 07:00-08:00 
 Now if we go over a look a little further, the tra c that's coming into that network is coming in via 
 our sensor. Let's have a look at our Modular Sensor.  System | Sensors  , and we can see we have SC 
 Modular Sensor 192. That's the name of the network it's sitting on. We can see here it is sitting with an 
 address of 192.168.1.235. All of those devices are sitting on the same network, the 192.168.1.0 network. 
 They're all participating in this vSwitch0, which is communicating out to the network via vmnic0. 
 That's the current setup that we're looking at. Now is there anything else in our UI I would like to show 
 you? I think if we just went to  Resources  , we'll just  see that there is, there is our two resources with 
 their addresses: 
 08:00-09:00 
 …the 192.168.1.233 for the DA 234 for the DL, and we saw before that our sensor was the 235. They're 
 all like one IP address apart. Okay. Let's jump in and have a look at our ESXi box. Here is our ESXi. We 
 can see our virtual machines. We've got our two virtual machines: our Stellar Cyber Data Lake 
 master and our Stellar Cyber Data Analyzer master, but let's ﬁrst of all go and look at the networking 
 that's conﬁgured. We talked about that vmnic0. Here are our physical NICs. You can see vmnic0 is the 
 only one that is connected and up and running. All the rest of them have linked down. There's a lot of 
 networking ports on this physical box, but only one of them is up and running. 
 09:00-10:00 
 So you say, “Well, how are we going to go from having only one interface to achieving this second 
 one?” Well, because we don't have another physical ESXi box with more virtual machines, we actually 
 don't need this piece. We don't need this external cluster and we don't actually need this vmnic1. 
 Really what we're going to create is just this additional virtual switch and these additional interfaces 
 on these VM. Any communication between the Data Analyzer and the Data Lake will happen via that 
 switch. That's what we're going to be looking at trying to achieve. Okay. That's our one physical 
 switch. We don't have to worry about vmnic1. It's not plugged into anything, but we would of course 
 do that if we had to scale and expand this Data Processor to a wider hardware availability with more 
 virtual machines, more working nodes, maybe a coordinating node. We're not going to do that right 
 now. 
 10:00-11:00 
 Let's look at virtual switches. Virtual switches: We have vSwitch0. That's the default switch that comes 
 in ESXi and we can see we have three port groups connected to it and one uplink. Well, we just saw 
 the uplink was that physical NIC. Let's look at the port groups that are connected to it. We have three 
 ADM-01-01-224  51 


---

<!-- Página 52 -->

 port groups: We have the management network, VM network, and the Stellar Cyber management 
 interface. Going back to our diagram, this is what we've got currently right now. We did identify that 
 it's vmnic0. And the port group is not VM Network. We're actually using Stellar Cyber Management in 
 that, but they're all using the same virtual switch. Any communication of any device that's coming in 
 from vmnic0 into the switch, will come into one of these three interfaces, but they're all sharing that 
 same information. 
 11:00-12:00 
 If we want to improve upon that and have some more scalability, we're going to add this vSwitch 
 cluster down at the bottom there. Okay. Now if we go look at our actual virtual machines, here's our 
 Data Analyzer. You see one network card. If we look at the Data Lake, same thing: one network card. 
 That's why it looks like this conﬁguration here. We have a DA and a DL with one network card that is 
 connecting to vSwitch0. Let's jump into the consoles of these devices. Here's our DA. Let's jump in 
 there.  Aella  . What we're going to do in here is a  show interface  . We can see we only have that 
 one interface. If we do a  show interface  , just that  one interface, that management interface, 
 192.168.1.233. 
 12:00-13:00 
 We close that and go have a look at our Data Lake. Open up its virtual console.  aella  . Do a  show 
 status  , show that it's all up and happy and working.  Yep. Already, great.  show interface  Just the 
 one interface  show interface all  , and still just that  one interface, the 192.168.1.234. Okay. What we 
 need to do is now go ahead. The one other thing we want to do is a  show cm  because this will be 
 something that changes. You can see that the cm here is to .234, which is the management IP address 
 of our Data Lake. Now if I close that and do the same thing on the Data Analyzer. 
 13:00-14:00 
 Let's open that up and do a  show cm  . We can see that  it is pointing. Although the Data Analyzer here 
 is 192.168.1.233, the cm is pointing to the management interface of the Data Lake, the 192.168.1.234. 
 Okay. Those are some of the things…I want to show you those because they're some of the things 
 that are going to change. Alright. Let's go and start making these changes. The ﬁrst thing we need to 
 do is we need a new virtual switch. We go to  Networking  ,  virtual switches  , and add a virtual switch 
 (select  Add standard virtual switch - New switch  ).  What are we going to call it? Well, let's call this 
 vSwitch-Cluster. That's going to be our cluster switch. 
 14:00–15:00 
 Now it adds an uplink here. Uplink 1 is to vmnic1. Now that's down because as we know nothing's 
 connected to it, we could even leave it there or we could remove it. Just to prove in this example that 
 you don't actually even need an external interface connected to it, let's remove it. We're going to just 
 remove that so it is just a virtual switch that's inside of this ESXi box only. Of course if we had those 
 scalable worker nodes, coordinating nodes on a di erent physical ESXi box, we would need of course 
 to add an uplink there. But let's just add it without an uplink. Bingo! We can see up here, “Virtual 
 switch was successfully created.” There it is, but nothing's connected to it. To achieve that, if we come 
 back to our diagram that we're looking for, to achieve that so great. We've created our vSwitch 
 cluster. Now we need a couple of interfaces here. 
 ADM-01-01-224  52 


---

<!-- Página 53 -->

 15:00-16:00 
 Well, when I say a couple, we only actually need one and both VMs will share that. Let's go ahead into 
 port groups and create an interface. We're going to add a port group. We're going to call it…let's stick 
 with our naming convention…Stellar Cyber, let's call it cluster. Now, it's not going to be connected to 
 vSwitch0. We're going to connect to the virtual switch that we just created: vSwitch cluster. That's all 
 we need to do there. What we've done so far is we've added a virtual switch vSwitch cluster. We can 
 now see there's one port bound to it. We removed the uplinks. There's no uplink connected to it. We 
 go to our port group and we can see our Stellar Cyber cluster is connected or bound to the virtual 
 switch vSwitch cluster. The next thing we need to do is go and add those interfaces to our VMs. 
 16:00-17:00 
 We now need to add this Stellar Cyber cluster interface or port group, we need to add that to both of 
 our virtual machines. We're going to go to our virtual machines. The ﬁrst thing we're going to do is 
 we're going to shut them down. Let's select them all and select  Shut down  . Alright. We can see now 
 that the little play button has gone next to them, that they've both been shut down. Let's do the Data 
 Lake Master ﬁrst. If we look at that we can see the fact that we've got the  Power on  button, which 
 means it's been shut down. Let's add this additional network adapter.  Edit  . We're going to add a 
 network adapter. 
 17:00-18:00 
 That's all we have to do because it automatically bound the Stellar Cyber cluster interface to that 
 adapter. That wasn’t much to do there. Click  Save  .  That was the Data Lake. Let's go to the Data 
 Analyzer. We can see up there it was successful, good to know. We're going to go to our Data 
 Analyzer. We're going to edit that because we can see there is only one network adapter. We are 
 going to add a network adapter, network adapter. It's already chosen the Stellar Cyber cluster. There 
 are other ones to choose. This is an ESXi thing. Maybe that's just the last port group that was created 
 so it selects that to be helpful to you and deﬁnitely we want it connected when we boot this system. 
 We've now got a DA with two network adapters. 
 18:00-19:00 
 We have a DL with two network adapters. We will now turn them on. I'm going to select both of them 
 and power on. We can go and see are they powering on? Let's look at one of them. This is the Data 
 Lake. Let's look at its console. We can see it's started to boot. Let's move its console over here and 
 we'll also do the same for…I don't want to move it o  the screen. Wow. That booted pretty quickly. 
 We'll go to the DA  and see where it is up to. It is also booted in this up and running. Let's start with 
 the Data Lake. Alright. Over here to  aella  . 
 19:00-20:00 
 Then we are now if we do a  show status  , this will  be in the process of loading the pods. It will 
 certainly not be up and running. Let's at least have a look. Clearly it is busy getting those pods up and 
 running rather than responding to my  show status  command.  While we're waiting for that, let's 
 jump in here and also…  aella  Okay. We'll do a  show  status  here too. Okay. We can see here that– 
 ADM-01-01-224  53 


---

<!-- Página 54 -->

 wow! That was really quick for the Data Lake. All pods are running, 89 images installed. We're just 
 waiting for the NTP and for the cluster to come up and running. 
 20:00-21:00 
 Let's see. Where do we get over here? This has got 11 pods running, expecting at least 16. 15 running. 
 These are both going to be up and running pretty quickly. Let's just jump in and have a look. Just 
 waiting for those to come up. I'm going to wait for them to come up before we make any further 
 changes. We've got some conﬁguration changes that we have to make. Let's just make sure that 
 these come up and they're up and running and happy. Alright. There it is the Data Analyzer on the 
 race. It came up ﬁrst. Or maybe it was just the ﬁrst one to show me that it was up and running ﬁrst. 
 Both of them are up and running. Okay. Let's do a  show interface  . Doesn't look much di erent 
 there.  Show interface  . Doesn't look much di erent  there but if we do a  show interface all  … 
 21:00-22:00 
 …we now have a new interface and we can see there is a link down. We've got this interface ENS 224 
 show interface all  . Alright. Same thing. We have an  interface, but it is currently down. Alright. 
 We'll do the Data Lake conﬁguration ﬁrst. The ﬁrst thing we're going to do is to and we're just going 
 to come back here and just conﬁrm what we're doing. We are telling the DA and the DL that it'll 
 communicate via their cluster interface using that new ENS 224 interface. That's what we're going to 
 use to communicate, which will be connected to that vSwitch cluster. That's what we're doing here. 
 Alright. First thing to do,  set cluster_interface  ENS224  . 
 22:00-23:00 
 If I've done that correctly, yes. Okay. Success! The next thing we do is we've got to give that interface 
 an IP address. We're going to do a  set interface cluster  IP  address of let's do  172.16.16  . 
 and let's keep the address over here the same. This is  .234  . Let's make this  234/24  . An entirely 
 di erent IP address. And  Enter  . Now we will do that  reboot and reset, but just a couple of other 
 commands We're going to do a  set cm  to be  172.16.16  ,  this address here that we just used  234  , 
 and  Enter  . Alright. If we do a  show cm  , that's what  we're expecting to see. 
 23:00-24:00 
 Now we've got to do the reboot and the reset. Let's start with that while we're waiting so reset. Sorry, 
 no. We want to reboot ﬁrst. Apologies, we want to reboot. Let that happen there. Now while that's 
 rebooting Let's come over here to our Data Analyzer. Okay. Same thing. We've got to tell it to use this 
 new interface as the interface to communicate as a cluster. We're going to do a  set cluster 
 interface–  I'm pressing tab to expand those commands–to  ens224  and  Enter  . We've had success 
 there. Fantastic. Let's give it an address.  Set interface  cluster IP  of 172.16.16… 
 24:00-25:00 
 ….233 to match the 233 of our 192.168/24. There's no actual reason to match but just thought we'd try 
 and show some consistency there with a /24. We now have that done. Okay. If we do a  show cm  , the 
 cm is no longer 192.168.1.234. The  set cm  is 172.16.16.234  as in the DL’s cluster interface. And  Enter  . 
 Alright. A  show CM  now will show a script thing. Okay.  Like it asked us to do with the Data Lake, we're 
 ADM-01-01-224  54 


---

<!-- Página 55 -->

 going to do a reboot and a reset.  reboot  . Now while that Data Analyzer is rebooting, let's come back 
 over here.  Aella  . 
 25:00-26:00 
 We're going to log in here  show interface all  , and  we can see that we have our two interfaces. 
 This time, our link is up with our IP addressing of 172.16.16.234, but we're going to have to wait for 
 everything else to come up. We do a  show status  .  It'll  be a while for this to come up. Okay. It is still 
 right in the pods. Okay. Nearly there: 36 of 39.  aella  .  Over here on the left we're back to our Data 
 Analyzer. We do a  show interface all  , and we can see  that is up. They are able to communicate 
 to each other. The 172.16.16.0 network we've got the Data Lake 234… 
 26:00-27:00 
 …and our Data Analyzer of 233 and they're both up and running. Alright. Let's do a  show status  . 
 Let's see how that's going. Okay So that's still in a boot situation too. Okay I'll just wait for these to 
 come up and running. We're just waiting for the NTP service to come up and sync. There's the Data 
 Lake up and running. We did boot the Data Lake ﬁrst, but the Data Analyzer has fewer pods to get up 
 and running. You can see it's still got 15 running of at least 16. Okay. There you can see we now have 
 a Data Analyzer that is system ready with all its pods up and running. Let's jump into the UI. 
 27:00-28:00 
 You were on the UI. I can't imagine that's where we last were, but let's refresh this because we have 
 booted the device since then. Okay. Are we all up and running and happy? Let's have a look. First of 
 all, we'll jump in here and have a look. All looks green here. We can see our machine learning services 
 are still loading. That's sitting there at 55 percent. We'll come back and look at that. Let's have a look 
 at our sensor. Is it up and running? Yes. Green and all good. Let's check-in  Investigate | Threat 
 Hunting  to see that we have tra c coming in. These  dips here are probably where we were doing 
 our reboots. We can see we have tra c coming into the network. We have data coming in. Let's go 
 ahead and have a look at our Data Lake and our Data Analyzer. 
 28:00-29:00 
 Okay. System let's look at our Data Lake ﬁrst. We go to Data Lake. Alright. We have our cluster up 
 and running happy with our 192.168.234. Nothing out of the ordinary there. We look at our node list 
 and now we can see that we have a Data Lake of 172.16. That's how they're communicating on that 
 234. A bit of a change there. Now let's go ahead and look at our Data Analyzer. We can see our Data 
 Analyzer is 192.168.1.233. We look at its node list. In there we can see its address of 172 and this is its 
 cluster interface address of 172.16.16.233. Those interfaces are these ones that we've conﬁgured here. 
 29:00-30:00 
 We've conﬁgured one for the Data Analyzer, one for the Data Lake. Two three four for the Data Lake 
 233 on the 172.16.16/24 network that's communicating to our vSwitch cluster. We can see that we have 
 adaptor 1 and adapter 2 for our Data Analyzer connected and connected. If we go look at our Data 
 Lake, we have adaptor 1 adapter and 2 connected and connected. All is working as expected. Now if 
 we go and look at the actual interface to show that there's tra c going across this second adapter, 
 ADM-01-01-224  55 


---

<!-- Página 56 -->

 this Stellar Cyber cluster connected, one of the only places we can see that is in the console or the 
 CLI of the Data Lake or the Data Analyzer. If we come in here and do a  show interface  … 
 30:00-31:00 
 …we can see there that our cluster down at the bottom RX bytes and TX bytes has increased. This has 
 received 1.2 gig and transmitted 40 megabytes. If we do that, do we see it grow? It’s probably di cult 
 to watch it grow from here. Well, the 40.3 has gone to 40.4. The only devices that are communicating 
 on that network. Remember it's a virtual network. There's nothing physical connected to it except for 
 these two virtual machines. Here we're looking at the Data Analyzer 1.2 and 40.7. Let's have a look at 
 the interface on the Data Lake. We'll try and put it back over there where it was before so you can 
 see them together. Line them up and line this guy up over here. We do a  show interface  . 
 31:00-32:00 
 You can see there that it sort of makes sense, right? One of them is the Data Analyzer has received 
 1.2 gig and the Data Lake has sent 1.1. I’m not sure exactly how the networking is counted there, sort 
 of makes sense to me. Alright. That is it for adding. We'll go back to our PowerPoint for adding that 
 virtual switch to an environment that was a basic setup of only having one switch. We added a 
 second switch with additional port groups. We added those port groups to the Data Analyzer and the 
 Data Lake. We are now in a position where we have a more scalable environment. If we were to then 
 further scale this with worker nodes and coordinating nodes on another ESXi box, we would have to 
 go in and add this vmnic1 back to our cluster. 
 32:00-33:00 
 Not a di cult thing to do at all there. We'd simply go back in to our virtual switch.  Networking  | 
 Virtual switches  . Let me close that console page.  We'd go into our vSwitch cluster. Have a look at 
 that, edit the settings, and we would add…let's just add it now. We would add an uplink. It's going to 
 choose vmnic1. Select  Save  . That's it. Now we'll see  that this should have a physical interface. Come 
 the time that we expand and we plug into vmnic1, we would have vmnic1 able to go communicate to 
 an external switch with another or two or three ESXi boxes to scale our Stellar Cyber platform. Thank 
 you. 
 The extended content lesson,  Reconﬁguring  the Data Processor  ,  is complete. Thank you. 
 ADM-01-01-224  56 


---