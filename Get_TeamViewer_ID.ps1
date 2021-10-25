$key = 'SYSTEM\CurrentControlSet\Control\Lsa'
$valuename = 'Security Packages'
$computers = Get-Content Servers.txt
foreach ($computer in $computers) {
	$reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', $computer)
	$regkey = $reg.opensubkey($key)
	$regkey.getvalue($valuename)
}