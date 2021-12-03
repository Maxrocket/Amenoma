pyinstaller -w -D --clean --add-data "model_artifact.h5;." --add-data "model_material.h5;." --add-data "Tools/ReliquaryLevelExcelConfigData.json;./Tools" --add-data "Tools/ReliquaryAffixExcelConfigData.json;./Tools" --add-data "rcc/genshin.ttf;./rcc" --hidden-import=h5py --hidden-import=h5py.defs --hidden-import=h5py.utils --hidden-import=h5py.h5ac --hidden-import=h5py._proxy --uac-admin -n Amenoma UImain.py