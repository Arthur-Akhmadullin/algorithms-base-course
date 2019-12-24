# получает на вход неотсортированный массив,
# по размеру соответствующий полностью заполненному дереву некоторой глубины,
# и выдаёт на выходе массив, содержащий структуру сбалансированного BST
def GenerateBBSTArray(a):
    a.sort()
    result_array = []
    depth = 0 #текущая глубина дерева
    while len(a) // 2**depth > 0:
        central_elements = []
        for elem in a[len(a) // 2**(depth + 1):: (len(a) // 2**depth) + 1]:
            central_elements.append(elem)
        result_array.extend(central_elements)
        depth += 1
    return result_array