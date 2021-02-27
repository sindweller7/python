# _*_ coding=utf-8 _*_
import re

def example():
    #index.html是从电子书的epub文件转换得到的
    with open('index.html', encoding='utf-8') as f_obj1:
        content = f_obj1.read()
        p_content = '(<table class="term"><tbody class="calibre16"><tr class="calibre17">' \
                    '\<td class="term1"><pre class="calibre33">.*?</pre>.*?</td>.*?</tr>.*?</tbody>.*?</table>)'
        results = re.findall(p_content, content, re.S)
    a = len(results)
    b = 0
    print(len(results))

    #不清楚为什么数据一次洗不干净,只能多次清洗
    while (b < a):
        a = len(results)
        for result in results:
            if '范例' not in result:
                results.remove(result)
            b = len(results)
        print(b)

    with open('result.html','w',encoding='utf-8') as f_obj2:
        num = 1
        for result in results:
            f_obj2.write('----------------------------------------------------------------------------------------------------')
            f_obj2.write(result)
            f_obj2.write('----------------------------------------------------------------------------------------------------')
            f_obj2.write('<br/>')
            num += 1

if __name__ == '__main__':
    example()
