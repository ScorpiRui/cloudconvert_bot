import cloudconvert

cloudconvert.default()

def converterr(vid):
    return cloudconvert.Job.create(payload={
        "tasks": {
            'import-my-file': {
                'operation': 'import/url',
                'url': f'{vid}'
            },
            'convert-my-file': {
                'operation': 'convert',
                'input': 'import-my-file',
                'output_format': 'mov',
                'some_other_option': 'value'
            },
            'export-my-file': {
                'operation': 'export/url',
                'input': 'convert-my-file'
            }
        }
    })
natija = converterr('https://youtu.be/4R7vRFGJr3k?si=Yg83AM82EGD916Wu')
print(natija)
if type(natija) is dict:
    exported_url_task_id = natija['id']
    res = cloudconvert.Task.wait(id=exported_url_task_id)  # Wait for job completion
    file = res.get("result").get("files")[0]
    res = cloudconvert.download(filename=file['filename'], url=file['url'])
    print(res)
