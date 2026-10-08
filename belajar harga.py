supply = 1_000_000_000
harga = 0.001

market_cap = supply * harga

token_creator = 400_000_000
nilai_creator = token_creator * harga

print("=== INFORMASI TOKEN ===")
print(f"Supply           : {supply:,} token")
print(f"Harga            : ${harga:.4f}")
print(f"Market Cap       : ${market_cap:,.2f}")
print()
print("=== CREATOR ===")
print(f"Token Creator    : {token_creator:,} token")
print(f"Nilai Token      : ${nilai_creator:,.2f}")


# Pembelian
token_dibeli = 100_000_000
harga_setelah_beli = 0.002

market_cap_setelah_beli = supply * harga_setelah_beli
nilai_creator_setelah_beli = token_creator * harga_setelah_beli

print()
print("=== SETELAH ADA PEMBELIAN ===")
print(f"Token dibeli          : {token_dibeli:,} token")
print(f"Harga baru            : ${harga_setelah_beli:.4f}")
print(f"Market Cap baru       : ${market_cap_setelah_beli:,.2f}")
print(f"Nilai token creator   : ${nilai_creator_setelah_beli:,.2f}")

# Creator menjual token
token_dijual = 100_000_000
harga_jual = harga_setelah_beli

uang_didapat = token_dijual * harga_jual

print()
print("=== CREATOR MENJUAL TOKEN ===")
print(f"Token dijual       : {token_dijual:,} token")
print(f"Harga jual         : ${harga_jual:.4f}")
print(f"Uang didapat       : ${uang_didapat:,.2f}")


# Simulasi liquidity
liquidity = 20_000

print()
print("=== LIQUIDITY ===")
print(f"Liquidity          : ${liquidity:,.2f}")
print(f"Nilai token dijual : ${uang_didapat:,.2f}")

if uang_didapat > liquidity:
    print("PERINGATAN: Nilai token yang dijual lebih besar daripada liquidity!")
else:
    print("Penjualan masih di bawah liquidity.")
    
# Simulasi dampak penjualan
persentase_dampak = uang_didapat / liquidity

harga_setelah_jual = harga_jual / (1 + persentase_dampak)

uang_didapat_simulasi = token_dijual * harga_setelah_jual

print()
print("=== SIMULASI DAMPAK PENJUALAN ===")
print(f"Liquidity              : ${liquidity:,.2f}")
print(f"Nilai penjualan awal   : ${uang_didapat:,.2f}")
print(f"Persentase dampak      : {persentase_dampak:.2f}x")
print(f"Harga sebelum jual     : ${harga_jual:.4f}")
print(f"Harga setelah jual     : ${harga_setelah_jual:.4f}")
print(f"Uang diterima           : ${uang_didapat_simulasi:,.2f}")


def simulasi_jual(token_dijual, harga, liquidity):
    nilai_jual = token_dijual * harga

    dampak = nilai_jual / liquidity

    harga_setelah = harga / (1 + dampak)

    uang_diterima = token_dijual * harga_setelah

    return harga_setelah, uang_diterima


print()
print("=== PERBANDINGAN PENJUALAN CREATOR ===")

harga = 0.002
liquidity = 20_000
token_creator = 400_000_000

penjualan = [0.10, 0.25, 0.50, 1.00]

for persen in penjualan:
    token_dijual = token_creator * persen

    harga_setelah, uang_diterima = simulasi_jual(
        token_dijual,
        harga,
        liquidity
    )

    print()
    print(f"Jual {persen:.0%} token")
    print(f"Token dijual      : {token_dijual:,.0f}")
    print(f"Harga setelah jual: ${harga_setelah:.6f}")
    print(f"Uang diterima     : ${uang_diterima:,.2f}")
    
    print()
print("=== PENGARUH LIQUIDITY ===")

harga = 0.002
token_creator = 400_000_000

liquidity_list = [20_000, 100_000, 500_000, 1_000_000]

for liquidity in liquidity_list:

    token_dijual = token_creator * 0.50

    harga_setelah, uang_diterima = simulasi_jual(
        token_dijual,
        harga,
        liquidity
    )

    print()
    print(f"Liquidity          : ${liquidity:,.2f}")
    print(f"Token dijual       : {token_dijual:,.0f}")
    print(f"Harga setelah jual : ${harga_setelah:.6f}")
    print(f"Uang diterima      : ${uang_diterima:,.2f}")
    
    token_pool = 1_000_000
uang_pool = 10_000

k = token_pool * uang_pool

print("=== KONDISI AWAL ===")
print(f"Token dalam pool : {token_pool:,}")
print(f"Uang dalam pool   : ${uang_pool:,.2f}")
print(f"Nilai k           : {k:,}")

# Creator menjual 100.000 token
token_dijual = 100_000

token_pool_baru = token_pool + token_dijual

uang_pool_baru = k / token_pool_baru

uang_diterima = uang_pool - uang_pool_baru

harga_awal = uang_pool / token_pool
harga_akhir = uang_pool_baru / token_pool_baru

print()
print("=== SETELAH CREATOR MENJUAL ===")
print(f"Token dijual      : {token_dijual:,}")
print(f"Uang diterima     : ${uang_diterima:,.2f}")
print(f"Harga awal        : ${harga_awal:.6f}")
print(f"Harga akhir       : ${harga_akhir:.6f}")


token_pool = 1_000_000
uang_pool = 10_000

k = token_pool * uang_pool

# Seseorang membeli 100.000 token
token_dibeli = 100_000

token_pool_baru = token_pool - token_dibeli

uang_pool_baru = k / token_pool_baru

uang_dibayar = uang_pool_baru - uang_pool

harga_awal = uang_pool / token_pool
harga_akhir = uang_pool_baru / token_pool_baru

print("=== PEMBELIAN ===")
print(f"Token dibeli       : {token_dibeli:,}")
print(f"Uang yang dibayar  : ${uang_dibayar:,.2f}")
print(f"Harga awal         : ${harga_awal:.6f}")
print(f"Harga akhir        : ${harga_akhir:.6f}")