# coding:utf-8
import os
import jinja2
import yaml

# 当前脚本路径
basepath = os.path.dirname(os.path.realpath(__file__))
# yaml文件夹
yamlPagesPath  = os.path.join(basepath, "pageelement")

def get_page_list(yamlpage):
    """
    function:把yal对象转成需要的页面对象数据：页面对象--》定位list
    args:yaml解析的对象--》dict类型
    return:    
    """
    page_object = {}
    for page, names in yamlpage.items():
        loc_names = []
        #获取所有的loctors定位方法
        locs = names["locators"]
        #添加定位name到列表
        for loc in locs:
            loc_names.append(loc['name'])
        page_object[page] = loc_names
    return page_object

def create_pages_py(page_list):
    """
    function:把jinja2把templatepage模板生成pages.py文件
    args:传get_page_list返回的内容:
    return:None    
    """
    print(os.path.join(basepath,"templetpage"))
    template_loader = jinja2.FileSystemLoader(searchpath=basepath)
    template_env = jinja2.Environment(loader=template_loader)

    templateVars = {
                'page_list':page_list
                }
    template = template_env.get_template("templetpage")
    with open(os.path.join(basepath,"pages.py"), 'w', encoding='utf-8')as f:
        f.write(template.render(templateVars))

def parseyaml():
    '''
    遍历读取yaml文件
    '''
    pageElements = {}
    # 遍历读取yaml文件
    for fpath, dirname, fnames in os.walk(yamlPagesPath):
        for name in fnames:
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath, name)
            # 排除一些非.yaml的文件
            if ".yaml" in str(yaml_file_path):
                with open(yaml_file_path, 'r', encoding='utf-8') as f:
                    page = yaml.load(f)
                    pageElements.update(page)
    return pageElements

if __name__ == "__main__":
    a = parseyaml()  
    b = get_page_list(a)  
    create_pages_py(b)
   
    
   