import os
import shutil

src_dir = "/Users/chenchunchih/碳永續/碳導遊"
dst_dir = os.path.join(src_dir, "videos")
os.makedirs(dst_dir, exist_ok=True)

mapping = {
    # 小半天系列 EP1-EP6
    "小半天_EP1_世外桃源由來.mp4": "xbt_ep1_origin.mp4",
    "小半天_EP2_孟宗竹海長源圳.mp4": "xbt_ep2_bamboo.mp4",
    "小半天_EP3_德興瀑布與雙瀑.mp4": "xbt_ep3_waterfall.mp4",
    "小半天_EP4_凍頂烏龍茶香傳奇.mp4": "xbt_ep4_tea.mp4",
    "小半天_EP5_石馬公園與竹藝傳奇.mp4": "xbt_ep5_sakura_bamboo.mp4",
    "小半天_EP6_兩天一夜低碳全攻略.mp4": "xbt_ep6_itinerary.mp4",
    
    # 碳導遊小綠系列 EP1-EP7
    "碳導遊小綠_EP1_旅行社也要算碳.mp4": "xl_ep1_travel_carbon.mp4",
    "碳導遊小綠_EP2_範疇一自家排的碳.mp4": "xl_ep2_scope1.mp4",
    "碳導遊小綠_EP3_範疇二買來的電.mp4": "xl_ep3_scope2.mp4",
    "碳導遊小綠_EP4_範疇三上下游的碳.mp4": "xl_ep4_scope3.mp4",
    "碳導遊小綠_EP5_碳足跡的邊界.mp4": "xl_ep5_boundary.mp4",
    "碳導遊小綠_EP6_動手算一趟旅程.mp4": "xl_ep6_calculation.mp4",
    "碳導遊小綠_EP7_總整理.mp4": "xl_ep7_summary.mp4",
}

for src_name, dst_name in mapping.items():
    src_file = os.path.join(src_dir, src_name)
    dst_file = os.path.join(dst_dir, dst_name)
    if os.path.exists(src_file):
        # copy or hardlink
        if not os.path.exists(dst_file):
            try:
                os.link(src_file, dst_file)
                print(f"Hardlinked {src_name} -> {dst_name}")
            except Exception:
                shutil.copy2(src_file, dst_file)
                print(f"Copied {src_name} -> {dst_name}")
        else:
            print(f"Already exists: {dst_name}")
    else:
        print(f"Not found: {src_name}")

print("\nListing videos in videos/ directory:")
for f in os.listdir(dst_dir):
    fp = os.path.join(dst_dir, f)
    sz = os.path.getsize(fp) / (1024*1024)
    print(f" - {f}: {sz:.1f} MB")
