from StringHelper import StringHelper;
from UnityFont import UnityFont;
from UnityText import UnityText;
import os;

def get_file_list(dir, list):
	if os.path.isfile(dir):
		list.append(dir)
	elif os.path.isdir(dir):
		for sub in os.listdir(dir):
			new_dir = os.path.join(dir, sub)
			get_file_list(new_dir, list)
	return list;

def gen_fon():
	sh = StringHelper();
	sh.code = "dos";
	for f in get_file_list("Text", []):
		if os.path.splitext(f)[-1] == '.xml' or os.path.splitext(f)[-1] == '.txt':
			sh.add_file_text(f);
	sh.add_western();

	str = sh.get_chars();

	# sfnttool.jar cant recognize relative path and 
	# the command line must be ansi encoded.
	font_path = os.getcwd().replace("/", "\\") + "\\Text\\";
	path = "E:\\Python Localization Helper\\Font\\"
	tool_path = "\"" + path + "sfnttool.jar\"";
	str = "\"" + str + "\"";

	# minify font
	commandstr = "java -jar " + tool_path + " -s " + str + " \"" + path + "SourceHanSansSC-Bold.ttf\" \"" + font_path + "SourceHanSansSC-Bold.ttf\""
	os.system(commandstr.encode('mbcs'))
	commandstr = "java -jar " + tool_path + " -s " + str + " \"" + path + "SourceHanSansSC-ExtraLight.ttf\" \"" + font_path + "SourceHanSansSC-ExtraLight.ttf\""
	os.system(commandstr.encode('mbcs'))
	commandstr = "java -jar " + tool_path + " -s " + str + " \"" + path + "SourceHanSansSC-Heavy.ttf\" \"" + font_path + "SourceHanSansSC-Heavy.ttf\""
	os.system(commandstr.encode('mbcs'))
	commandstr = "java -jar " + tool_path + " -s " + str + " \"" + path + "SourceHanSansSC-Light.ttf\" \"" + font_path + "SourceHanSansSC-Light.ttf\""
	os.system(commandstr.encode('mbcs'))
	commandstr = "java -jar " + tool_path + " -s " + str + " \"" + path + "SourceHanSansSC-Medium.ttf\" \"" + font_path + "SourceHanSansSC-Medium.ttf\""
	os.system(commandstr.encode('mbcs'))
	commandstr = "java -jar " + tool_path + " -s " + str + " \"" + path + "SourceHanSansSC-Normal.ttf\" \"" + font_path + "SourceHanSansSC-Normal.ttf\""
	os.system(commandstr.encode('mbcs'))
	commandstr = "java -jar " + tool_path + " -s " + str + " \"" + path + "SourceHanSansSC-Regular.ttf\" \"" + font_path + "SourceHanSansSC-Regular.ttf\""
	os.system(commandstr.encode('mbcs'))

	# generate unity font
	font = UnityFont("OriginalFile/unnamed asset-sharedassets1.assets-962.dat", unity_version = [4, 7, 0, 0], version = 9);
	font.convert_to_raw("ChainsawWarrior2/unnamed asset-sharedassets1.assets-962.dat", "Text/SourceHanSansSC-Medium.ttf");
	font = UnityFont("OriginalFile/unnamed asset-sharedassets1.assets-963.dat", unity_version = [4, 7, 0, 0], version = 9);
	font.convert_to_raw("ChainsawWarrior2/unnamed asset-sharedassets1.assets-963.dat", "Text/SourceHanSansSC-ExtraLight.ttf");
	font = UnityFont("OriginalFile/unnamed asset-sharedassets1.assets-964.dat", unity_version = [4, 7, 0, 0], version = 9);
	font.convert_to_raw("ChainsawWarrior2/unnamed asset-sharedassets1.assets-964.dat", "Text/SourceHanSansSC-Medium.ttf");
	font = UnityFont("OriginalFile/unnamed asset-sharedassets1.assets-965.dat", unity_version = [4, 7, 0, 0], version = 9);
	font.convert_to_raw("ChainsawWarrior2/unnamed asset-sharedassets1.assets-965.dat", "Text/SourceHanSansSC-Light.ttf");
	font = UnityFont("OriginalFile/unnamed asset-sharedassets1.assets-966.dat", unity_version = [4, 7, 0, 0], version = 9);
	font.convert_to_raw("ChainsawWarrior2/unnamed asset-sharedassets1.assets-966.dat", "Text/SourceHanSansSC-Heavy.ttf");
	font = UnityFont("OriginalFile/unnamed asset-sharedassets1.assets-967.dat", unity_version = [4, 7, 0, 0], version = 9);
	font.convert_to_raw("ChainsawWarrior2/unnamed asset-sharedassets1.assets-967.dat", "Text/SourceHanSansSC-Heavy.ttf");
	font = UnityFont("OriginalFile/unnamed asset-sharedassets1.assets-968.dat", unity_version = [4, 7, 0, 0], version = 9);
	font.convert_to_raw("ChainsawWarrior2/unnamed asset-sharedassets1.assets-968.dat", "Text/SourceHanSansSC-Regular.ttf");
	font = UnityFont("OriginalFile/unnamed asset-sharedassets1.assets-969.dat", unity_version = [4, 7, 0, 0], version = 9);
	font.convert_to_raw("ChainsawWarrior2/unnamed asset-sharedassets1.assets-969.dat", "Text/SourceHanSansSC-Bold.ttf");
	font = UnityFont("OriginalFile/unnamed asset-sharedassets1.assets-970.dat", unity_version = [4, 7, 0, 0], version = 9);
	font.convert_to_raw("ChainsawWarrior2/unnamed asset-sharedassets1.assets-970.dat", "Text/SourceHanSansSC-ExtraLight.ttf");
	font = UnityFont("OriginalFile/unnamed asset-sharedassets1.assets-971.dat", unity_version = [4, 7, 0, 0], version = 9);
	font.convert_to_raw("ChainsawWarrior2/unnamed asset-sharedassets1.assets-971.dat", "Text/SourceHanSansSC-Regular.ttf");
	
utxt = UnityText("OriginalFile/unnamed asset-resources.assets-120.dat");
utxt.load_from_txt("Text/en-resources.assets-120.xml");
utxt.save_to_raw("ChainsawWarrior2/unnamed asset-resources.assets-120.dat");

utxt = UnityText("OriginalFile/unnamed asset-resources.assets-128.dat");
utxt.load_from_txt("Text/TutorialXMLData-resources.assets-128.xml");
utxt.save_to_raw("ChainsawWarrior2/unnamed asset-resources.assets-128.dat");

utxt = UnityText("OriginalFile/unnamed asset-resources.assets-118.dat");
utxt.load_from_txt("Text/blessings-resources.assets-118.xml");
utxt.save_to_raw("ChainsawWarrior2/unnamed asset-resources.assets-118.dat");

utxt = UnityText("OriginalFile/unnamed asset-resources.assets-132.dat");
utxt.load_from_txt("Text/buffs-resources.assets-132.xml");
utxt.save_to_raw("ChainsawWarrior2/unnamed asset-resources.assets-132.dat");

utxt = UnityText("OriginalFile/unnamed asset-resources.assets-126.dat");
utxt.load_from_txt("Text/enemies-resources.assets-126.xml");
utxt.save_to_raw("ChainsawWarrior2/unnamed asset-resources.assets-126.dat");

utxt = UnityText("OriginalFile/unnamed asset-resources.assets-122.dat");
utxt.load_from_txt("Text/equipment-resources.assets-122.xml");
utxt.save_to_raw("ChainsawWarrior2/unnamed asset-resources.assets-122.dat");

utxt = UnityText("OriginalFile/unnamed asset-resources.assets-127.dat");
utxt.load_from_txt("Text/other_cards-resources.assets-127.xml");
utxt.save_to_raw("ChainsawWarrior2/unnamed asset-resources.assets-127.dat");

utxt = UnityText("OriginalFile/unnamed asset-resources.assets-123.dat");
utxt.load_from_txt("Text/traps-resources.assets-123.xml");
utxt.save_to_raw("ChainsawWarrior2/unnamed asset-resources.assets-123.dat");

gen_fon();