def new_project(params):
  # highway new [project_name]
  
  print(f'Creating new Flask Highway project called "{params[0]}"')
  import requests, os
  from zipfile import ZipFile

  try:
    proj = 'flask-highway-main'
    rp = os.path.realpath(__file__)
    rp = rp[:rp.rfind(os.sep)]
    zip_path = os.path.join(rp, 'app.zip')

    print('Verifying cached Flask Highway Base app')
    if not os.path.isfile(zip_path):
      print('Flask Highway Base app not found')
      print('Downloading from github. May take a while')
      url = 'https://github.com/alantelles/flask-highway/archive/main.zip'
      repo = requests.get(url)
      print('Download finished')
      print('Writing zip clone to disk')
      zip_app = open(zip_path, 'wb')
      zip_app.write(repo.content)
      print('Writing zip successfully written')

    else:
      print('Flask Highway base app found in cache')
      zip_app = open(zip_path, 'rb')

    zip_handler = ZipFile(zip_path)
    print('Extracting Flask Highway base app...')
    zip_handler.extractall()
    zip_handler.close()
    zip_app.close()
    print(f'Renaming directory to {params[0]}')
    os.rename(proj, params[0])
    print(f'New Flask Highway project "{params[0]}" initialized')

    cp = os.getcwd()
    lines = []
    conf_file = os.path.join(os.getcwd(), params[0], 'app', 'config.py')
    with open(conf_file, 'rt') as conf:
      for l in conf.readlines():
        if l.find('Flask Highway App') > 0:
          lines.append(l.replace('Flask Highway App', params[0]))
        else:
          lines.append(l)

    with open(conf_file, 'wt') as conf:
      conf.writelines(lines)
    
  except IndexError:
    raise IndexError('A name for your project was not provided')