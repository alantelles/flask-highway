from bin.constants import *
import os
import shutil
import traceback


def generate(params):
  opt = {
    'blueprint': blueprint,
    'views': views
  }
  handler = opt[params[0]]
  handler(params[1:])

def views(params):
  pass

def blueprint(params):
  # highway generate blueprint [blueprint_name]
  bp_name = params[0]
  bp_name_camel = [w.capitalize() for w in bp_name.split('_')]
  bp_name_camel = ''.join(bp_name_camel)
  nbp = f'{BPP}/{bp_name}'
  os.mkdir(nbp)
  routes = f'{nbp}/routes.yaml'
  os.mkdir(f'{nbp}/models')
  os.mkdir(f'{nbp}/templates')
  os.mkdir(f'{nbp}/templates/{bp_name}')
  os.mkdir(f'{nbp}/views')
  src = BP_INIT
  dest = f'{nbp}/__init__.py'
  shutil.copyfile(src, dest)
  with open(dest, 'rt') as bps:
    cont = []
    bp_name = params[0]
    for li in bps.readlines():
      cont.append(li.format(bp_name=bp_name, bp_name_camel=bp_name_camel))
          
  with open(dest, 'wt') as bps:
    bps.writelines(cont)
    
  src = BP_TP
  dest = f'{nbp}/templates/{bp_name}/index.html'
  shutil.copyfile(src, dest)
  with open(dest, 'rt') as tps:
    cont = []
    for li in tps.readlines():
      try:
        cont.append(
        li.format(
          bp_name_camel=bp_name_camel))
          
      except KeyError:
        cont.append(li)
      
  with open(dest, 'wt') as tps:
    tps.writelines(cont)
    
  with open(routes, 'wt') as rtf:
    rt_cont = [
      '# register your routes here\n',
      '# they will be loaded in app startup\n',
      '# no need to use conventional Flask routing\n',
      f'root: {bp_name}_views.index'
    ]
    rtf.writelines(rt_cont)

  with open(APP_INIT, 'rt') as apin:
    cont = apin.readlines()
    for i in range(len(cont)):
      if cont[i].strip() == "#DON'T REMOVE: blueprints register section":
        cont.insert(i+1, f'app.register_blueprint({bp_name})\n')
        cont.insert(i+1, f'from app.blueprints.{bp_name} import {bp_name}\n')
        break

  with open(APP_INIT, 'wt') as apin:
    apin.writelines(cont)
    
  print(f'Blueprint {bp_name} created')

# highway generate views [name] in [blueprint_name]
def views(params):
  try:
    view_name = params[0]
    conj = params[1]
    bp_name = params[2]
    

    if conj == 'in':
      bp_name_camel = [w.capitalize() for w in bp_name.split('_')]
      bp_name_camel = ''.join(bp_name_camel)
      view_name_camel = [w.capitalize() for w in view_name.split('_')]
      view_name_camel = ''.join(view_name_camel)
      views_list = '    pass\n'
      actions = []
      if len(params) > 3:
        actions = params[3]
        if actions != ':resource':
          actions = [action.strip() for action in actions.split(',')]
          views_list = ''
          template = """
    @render
    def {action}(self):
        pass
  """
          for action in actions:
            views_list += template.format(bp_name=bp_name, view_name=view_name, action=action)

      out = []
      vp = f'{BLPLTS}/py/blueprint.view.py'
      dest = f'{BPP}/{bp_name}/views/{view_name}.py'
      with open(vp, 'rt') as vwbp:
        
        for l in vwbp.readlines():
          out.append(l.format(view_name=view_name, bp_name=bp_name, view_name_camel=view_name_camel, views_list=views_list))

      with open(dest, 'wt') as vwbp:
        vwbp.writelines(out)

      os.mkdir(f'{BPP}/{bp_name}/templates/{bp_name}/{view_name}')

      with open(VW_TP, 'rt') as tps:
        tp_lines = tps.readlines()
        for action in actions:
          cont = []
          for li in tp_lines:
            try:
              cont.append(
              li.format(
                bp_name=bp_name, view_name_camel=view_name_camel, action=action))
                
            except KeyError:
              cont.append(li)
              pass

          with open(f'{BPP}/{bp_name}/templates/{bp_name}/{view_name}/{action}.html', 'wt') as tpp:
            tpp.writelines(cont)

      with open(f'{BPP}/{bp_name}/__init__.py', 'rt') as inbp:
        lines = inbp.readlines()

      for i in range(len(lines)):
        if lines[i].strip() == "#DON'T REMOVE: blueprint views register section":
          lines.insert(i+1, f'from app.blueprints.{bp_name}.views.{view_name} import {view_name}_views\n')
          continue

        if lines[i].strip() == "#DON'T TOUCH: register routes section":
          rgp = i + 1
          reg = lines[rgp].strip()
          reg = reg[:reg.rfind(')')]
          reg += f", {view_name}={view_name}_views)\n"
          lines[rgp] = reg

      with open(f'{BPP}/{bp_name}/__init__.py', 'wt') as inbp:
        inbp.writelines(lines)

    else:
        print('Connector not recognized')

  except KeyError:
    raise KeyError('Wrong number of arguments for this generator')

  pass
  