import subprocess

command_get = 'curl -X GET https://api.api-ninjas.com/v1/jokes?limit=1'

command_post = 'curl -X POST -H "Content-Type: application/json" -d ' + '{"key1":"value1","key2":"value2"} ' + 'https://www.example.com'


subprocess.run(['curl', '-X', 'GET', '-H', 'Content-Type: application/json', '-H', 'X-Api-Key: 6JCTO6nTPOeiaG1Nowrslw==dCPBai6zZOF2MiHA', 'https://api.api-ninjas.com/v1/jokes?limit=1'])

