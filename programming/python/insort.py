def insort(a):
    for i in range(len(a)-1):
        # 隣り合った要素 a[i] と a[i+1] を比べる。
        if a[i+1] < a[i]:
            # a[i+1] のほうが a[i] よりも小さい。
            x = a[i+1]
            # したがって、x の値を、a[0]〜a[i-1] までのどこかに挿入する。
            # 適切な位置 p を発見する。
            # これは現在の i より左にある要素を見ていく。
            p = i
            while (0 < p) and (x <= a[p-1]):
                p = p - 1
            # この時点で a[p] = x となるべきであるから
            # a[p]〜a[i] の要素をひとつずつ右にずらす。
            q = i
            while p <= q:
                a[q+1] = a[q]
                q = q - 1
            # 最後に a[p] を x とする。
            a[p] = x
    return
import sys
a = []
for i in range(len(sys.argv)-1):
    v = int(sys.argv[i+1])
    a = a + [v]
# ソートを実行し、結果を表示する。
insort(a)
print(a)
