cd 'C:\Users\kevinmoraes\Downloads\Analista SOC\Casos'
Get-ChildItem -File -Filter "*.md" | Where-Object { $_.Name -ne "SecurityOnion_Memoria_Institucional.md" } | ForEach-Object {
    $folderName = $_.BaseName
    New-Item -ItemType Directory -Force -Path $folderName
    Move-Item -Path $_.FullName -Destination "$folderName\alerta_original.md"
}
