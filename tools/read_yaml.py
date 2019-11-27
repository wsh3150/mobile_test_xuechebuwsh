import yaml


def build_login_data():
    """登录数据构造方法"""
    with open('./data/login_data.yaml', encoding='utf-8')as f:
        data = yaml.safe_load(f)
        data_list = []
        for i in data.values():
            data_list.append((i.get('name'),
                              i.get('pwd'),
                              i.get('expect'),
                              i.get('is_success')))
        print(data_list)
        return data_list


if __name__ == '__main__':
    build_login_data()
