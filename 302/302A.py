A, B = map(int, input().split())

# 敵の体力をBで割った商に1を足すことで必要な攻撃回数を求める
attacks = (A + B - 1) // B

print(attacks)
