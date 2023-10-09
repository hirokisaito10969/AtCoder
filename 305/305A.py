N = int(input())

# 給水所の位置のリストを作成
water_stations = [i * 5 for i in range(22)]

if N in water_stations:
    # Nが給水所の位置に一致する場合
    print(N)
else:
    # Nが給水所の位置と一致しない場合
    nearest_station = min(water_stations, key=lambda x: abs(x - N))
    print(nearest_station)
