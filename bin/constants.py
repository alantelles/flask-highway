import os

APPP = 'app'
BPP = f'{APPP}/blueprints'
TPS = f'{APPP}/templates'
LYT = f'{TPS}/layouts'
DTB = f'{APPP}/database'
STCS = f'{APPP}/static'
APP_INIT = f'{APPP}/__init__.py'

rp = os.path.realpath(__file__)
rp = rp[:rp.rfind(os.sep)]
BLPLTS = f'{rp}/boilerplates'
BP_INIT = f'{BLPLTS}/py/blueprint.__init__.py'
BP_TP = f'{BLPLTS}/html/blueprint.index.html'