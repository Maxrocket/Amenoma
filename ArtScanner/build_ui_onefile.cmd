set TARGET_VERSION=3.4.0
set DICT_TARGET_VERSION=v34

pyinstaller -w -F ^
--add-data "rcc/models_CHS/artifact_model_%TARGET_VERSION%.h5;./rcc/models_CHS" ^
--add-data "rcc/models_CHS/material_model_%TARGET_VERSION%.h5;./rcc/models_CHS" ^
--add-data "Tools/ReliquaryLevelExcelConfigData.json;./Tools" ^
--add-data "Tools/ReliquaryAffixExcelConfigData.json;./Tools" ^
--add-data "rcc/genshin.ttf;./rcc" ^
--add-data "rcc/material_names_%DICT_TARGET_VERSION%.json;./rcc" ^
--add-data "rcc/char_map_%DICT_TARGET_VERSION%.json;./rcc" ^
--hidden-import=h5py ^
--hidden-import=h5py.defs ^
--hidden-import=h5py.utils ^
--hidden-import=h5py.h5ac ^
--hidden-import=h5py._proxy ^
--uac-admin ^
-n Amenoma ^
UImain.py