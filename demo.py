from fairy_gui import *

# 加载一个FGUI项目
fgui_file_path:str = r"D:\FGUIProject\FGUIProject.fairy"
project:FGUIProject = FGUIProject(fgui_file_path)

# 获取项目的主分支（目前仅支持）
branch:FGUIBranch = project.main_branch

# 获取该分支下所有包
package_list:list[FGUIPackage] = branch.package_list

# 获取某个名字的包
master_package:FGUIPackage = branch.get_package_by_name("master")

# 获取指定url对应的资源
component_url:str = "ui://pkgidandresid"
resource:FGUIResource = branch.get_resource_by_url(component_url)

# 获取一个组件资源内部的元件
obj_list:list[FGUIObject] = resource.object_list
test_obj:FGUIObject = obj_list[0]

# 获取对其他资源的引用关系，会返回有效的引用资源和无效的引用资源
# 包层级的引用（包括包内所有资源，以及资源内所有元件）
pkg_ref_list, pkg_invalid_ref_list = master_package.get_references()
# 资源层级的引用（包括资源内所有元件）
res_ref_list, res_invalid_ref_list = resource.get_references()
# 元件层级的引用
obj_ref_list, obj_invalid_ref_list = test_obj.get_references()

# 你也可以判断一个对应的资源文件是否真的存在
if resource.file_exists is False:
    print("资源文件不存在")
else:
    print("资源文件存在于：" + resource.full_path)