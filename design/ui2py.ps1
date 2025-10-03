$OutputEncoding = [System.Text.Encoding]::UTF8
# 脚本说明：遍历ui文件和qrc文件并转换为py文件

$uiFiles = Get-ChildItem -Path ./ui -Filter *.ui
$count = $uiFiles.Count
Write-Host "`n*** 开始转换.ui ***" -ForegroundColor Red
$nums = 0
$res = ""
$uiFiles | ForEach-Object {
    $nums += 1
    Write-Host $_.BaseName "转换中... $nums/$count" -ForegroundColor Blue
    $outputPath = "./Ui_" + $_.BaseName + ".py"
    $res = pyside6-uic $_.FullName -o $outputPath 2>&1
    if ($res) {
        Write-Host $res "`n" -ForegroundColor Red
        break
    }
    if ($nums -eq $count) {
        Write-Host "*** .ui转换完成 ***`n" -ForegroundColor Green
    }
}

$qrcFiles = Get-ChildItem -Path ./assets -Filter *.qrc
$count = $qrcFiles.Count
Write-Host "*** 开始转换.qrc ***" -ForegroundColor Red
$nums = 0
$res = ""
$qrcFiles | ForEach-Object {
    $nums += 1
    Write-Host $_.BaseName "转换中... $nums/$count" -ForegroundColor Blue
    $outputPath = "../" + $_.BaseName + "_rc.py"
    $res = pyside6-rcc $_.FullName -o $outputPath 2>&1
    if ($res) {
        Write-Host $res "`n" -ForegroundColor Red
        break
    }
    if ($nums -eq $count) {
        Write-Host "*** .qrc转换完成 ***`n" -ForegroundColor Green
    }
}