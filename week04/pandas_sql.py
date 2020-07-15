import pandas as pd
import numpy as np
import random

city = [
    '深圳',
    '北京',
    '广州',
    '深圳'
]

gender = ['男', '女']


def genData1(num):
    datas = []
    for i in range(1, num+1):
        data = {'id': i, 'name': genName(), 'gender': random.choice(gender), 'age': np.random.randint(
            20, 60), 'order_id': '100000'+str(i)}
        datas.append(data)
    return datas


def genData2(num):
    datas = []
    for i in range(1, num+1):
        data = {'id': i, 'order_id': '100000'+str(i), 'city': random.choice(city), 'totally': np.random.randint(
            0, 500)}
        datas.append(data)
    return datas


def genName():
    np.random.seed()
    len = np.random.randint(3, 10)

    np.random.seed()
    num = np.random.randint(65, 91, len)
    name = [chr(i) for i in num]
    name = ''.join(name)
    return name


def main():
    # 模拟sql数据
    data1 = genData1(15)
    print('*' * 80)
    print('data1:')
    print(data1)
    pdata1 = pd.DataFrame(data1)
    print(pdata1)

    data2 = genData2(5)
    print('*' * 80)
    print('data2:')
    print(data2)
    pdata2 = pd.DataFrame(data2)
    print(pdata2)

    # 1. SELECT * FROM data;
    pdata1
    print('*' * 80)
    print('SELECT * FROM data')
    print(pdata1)

    # 2. SELECT * FROM data LIMIT(10);
    pdada_limitrow = pdata1.iloc[:10]
    print('*' * 80)
    print('SELECT * FROM data LIMIT(10)')
    print(pdada_limitrow)

    # 3. SELECT id FROM data;  //id 是 data 表的特定一列
    pdata_id = pdata1['id']
    print('*' * 80)
    print('SELECT id FROM data')
    print(pdata_id)

    # 4. SELECT COUNT(id) FROM data;
    pdata_count = len(pdata_id)
    print('*' * 80)
    print('SELECT COUNT(id) FROM data')
    print(pdata_count)
    print(pdata_id.size)

    # 5. SELECT * FROM data WHERE id<1000 AND age>30;
    pdata_id_aga = pdata1[(pdata1.id < 1000) & (pdata1.age > 30)]
    print('*' * 80)
    print('SELECT * FROM data WHERE id<1000 AND age>30')
    print(pdata_id_aga)

    # 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
    pdata1_id_orderid = pdata1.groupby('id').agg(
        {'order_id': pd.Series.nunique})
    pdata1_id_orderid.reindex(['id', 'order_id']).reset_index()
    print('*' * 80)
    print('SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id')
    print(pdata1_id_orderid)

    # 7. SELECT * FROM table1 t1 INNER_JOIN table2 t2 ON t1.id = t2.id;
    pdata_inner_join = pd.merge(pdata1, pdata2, how='inner', on='id')
    print('*' * 80)
    print('SELECT * FROM table1 t1 INNER_JOIN table2 t2 ON t1.id = t2.id')
    print(pdata_inner_join)

    # 8. SELECT * FROM table1 UNION SELECT * FROM table2;
    pds = [pdata1, pdata2]
    pdata_union = pd.concat(pds)
    print('*' * 80)
    print('SELECT * FROM table1 UNION SELECT * FROM table2')
    print(pdata_union)

    # 9. DELETE FROM table1 WHERE id=10;
    # pdata_delete = pdata1[(pdata1.id == 10)]
    pdata_new = pdata1.drop(pdata1[pdata1.id == 10].index)
    print('*' * 80)
    print('DELETE FROM table1 WHERE id=10')
    print(pdata_new)

    # 10. ALTER TABLE table1 DROP COLUMN column_name;
    pdata_new_column = pdata1.drop('gender', axis=1)
    print('*' * 80)
    print('ALTER TABLE table1 DROP COLUMN column_name')
    print(pdata_new_column)


if __name__ == "__main__":
    main()
