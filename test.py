import json
import os
import shutil

j='E:/KyungHee/test/json' #json파일 담긴 폴더 주소
p='E:/KyungHee/test/picture' #picture파일 담긴 폴더 주소
list_j=os.listdir(j)  #json폴더 하위 파일 이름 리스트 생성
len_j=len(list_j)    #리스트 길이
list_p=os.listdir(p)
len_p=len(list_p)

os.mkdir('E:/KyungHee/test/sep/퍼')   #소재 종류 파일 폴더 생성
os.mkdir('E:/KyungHee/test/sep/무스탕')
os.mkdir('E:/KyungHee/test/sep/스웨이드')
os.mkdir('E:/KyungHee/test/sep/앙고라')
os.mkdir('E:/KyungHee/test/sep/코듀로이')
os.mkdir('E:/KyungHee/test/sep/시퀸글리터')
os.mkdir('E:/KyungHee/test/sep/데님')
os.mkdir('E:/KyungHee/test/sep/저지')
os.mkdir('E:/KyungHee/test/sep/트위드')
os.mkdir('E:/KyungHee/test/sep/벨벳')
os.mkdir('E:/KyungHee/test/sep/비닐PVC')
os.mkdir('E:/KyungHee/test/sep/울캐시미어')
os.mkdir('E:/KyungHee/test/sep/합성섬유')
os.mkdir('E:/KyungHee/test/sep/니트')
os.mkdir('E:/KyungHee/test/sep/레이스')
os.mkdir('E:/KyungHee/test/sep/린넨')
os.mkdir('E:/KyungHee/test/sep/메시')
os.mkdir('E:/KyungHee/test/sep/플리스')
os.mkdir('E:/KyungHee/test/sep/네오프렌')
os.mkdir('E:/KyungHee/test/sep/실크')
os.mkdir('E:/KyungHee/test/sep/스판덱스')
os.mkdir('E:/KyungHee/test/sep/자카드')
os.mkdir('E:/KyungHee/test/sep/가죽')
os.mkdir('E:/KyungHee/test/sep/면')
os.mkdir('E:/KyungHee/test/sep/시폰')
os.mkdir('E:/KyungHee/test/sep/우븐')

fur='E:/KyungHee/test/sep/퍼'    #소재 종류 경로 변수
mustang='E:/KyungHee/test/sep/무스탕'
suede='E:/KyungHee/test/sep/스웨이드'
angora='E:/KyungHee/test/sep/앙고라'
corduroy='E:/KyungHee/test/sep/코듀로이'
sequin='E:/KyungHee/test/sep/시퀸글리터'
denim='E:/KyungHee/test/sep/데님'
jersey='E:/KyungHee/test/sep/저지'
tweed='E:/KyungHee/test/sep/트위드'
velvet='E:/KyungHee/test/sep/벨벳'
vinyl='E:/KyungHee/test/sep/비닐PVC'
wool='E:/KyungHee/test/sep/울캐시미어'
synthetic='E:/KyungHee/test/sep/합성섬유'
knit='E:/KyungHee/test/sep/니트'
lace='E:/KyungHee/test/sep/레이스'
linen='E:/KyungHee/test/sep/린넨'
mesh='E:/KyungHee/test/sep/메시'
fleece='E:/KyungHee/test/sep/플리스'
neoprene='E:/KyungHee/test/sep/네오프렌'
silk='E:/KyungHee/test/sep/실크'
spandex='E:/KyungHee/test/sep/스판덱스'
jacquard='E:/KyungHee/test/sep/자카드'
leather='E:/KyungHee/test/sep/가죽'
cotton='E:/KyungHee/test/sep/면'
chiffon='E:/KyungHee/test/sep/시폰'
woven='E:/KyungHee/test/sep/우븐'


for i in range(len_j):      #json파일 개수만큼 반복
    x=j+'/'+list_j[i]
    with open(x, 'rt', encoding='UTF8') as fp:    #json 읽어오기
        data = json.load(fp)

    if data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['아우터'][0].get('소재'):    #아우터, 하의, 원피스, 상의 아래에 소재정보 있으면 
        a=str(data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['아우터'][0]['소재']) #소재 정보 저장
        b=a[2:-2]
        if os.path.exists(p+'/'+list_j[i][:-5]+'.jpg') == 1:      #json 파일과 이름이 같은 사진파일이 있다면 
            if b == '퍼':                                         #소재 종류별로 소재 종류 파일 폴더에 복사
                shutil.copy(p+'/'+list_p[i], fur+'/'+list_p[i])
            elif b == '무스탕':
                shutil.copy(p+'/'+list_p[i], mustang+'/'+list_p[i])
            elif b == '스웨이드':
                shutil.copy(p+'/'+list_p[i], suede+'/'+list_p[i])
            elif b == '앙고라':
                shutil.copy(p+'/'+list_p[i], angora+'/'+list_p[i])
            elif b == '코듀로이':
                shutil.copy(p+'/'+list_p[i], corduroy+'/'+list_p[i])
            elif b == '시퀸/글리터':
                shutil.copy(p+'/'+list_p[i], sequin+'/'+list_p[i])
            elif b == '데님':
                shutil.copy(p+'/'+list_p[i], denim+'/'+list_p[i])
            elif b == '저지':
                shutil.copy(p+'/'+list_p[i], jersey+'/'+list_p[i])
            elif b == '트위드':
                shutil.copy(p+'/'+list_p[i], tweed+'/'+list_p[i])
            elif b == '벨벳':
                shutil.copy(p+'/'+list_p[i], velvet+'/'+list_p[i])
            elif b == '비닐/PVC':
                shutil.copy(p+'/'+list_p[i], vinyl+'/'+list_p[i])
            elif b == '울/캐시미어':
                shutil.copy(p+'/'+list_p[i], wool+'/'+list_p[i])
            elif b == '합성섬유':
                shutil.copy(p+'/'+list_p[i], synthetic+'/'+list_p[i])
            elif b == '니트':
                shutil.copy(p+'/'+list_p[i], knit+'/'+list_p[i])
            elif b == '레이스':
                shutil.copy(p+'/'+list_p[i], lace+'/'+list_p[i])
            elif b == '린넨':
                shutil.copy(p+'/'+list_p[i], linen+'/'+list_p[i])
            elif b == '메시':
                shutil.copy(p+'/'+list_p[i], mesh+'/'+list_p[i])
            elif b == '플리스':
                shutil.copy(p+'/'+list_p[i], fleece+'/'+list_p[i])
            elif b == '네오프렌':
                shutil.copy(p+'/'+list_p[i], neoprene+'/'+list_p[i])
            elif b == '실크':
                shutil.copy(p+'/'+list_p[i], silk+'/'+list_p[i])
            elif b == '스판덱스':
                shutil.copy(p+'/'+list_p[i], spandex+'/'+list_p[i])
            elif b == '자카드':
                shutil.copy(p+'/'+list_p[i], jacquard+'/'+list_p[i])
            elif b == '가죽':
                shutil.copy(p+'/'+list_p[i], leather+'/'+list_p[i])
            elif b == '면':
                shutil.copy(p+'/'+list_p[i], cotton+'/'+list_p[i])
            elif b == '시폰':
                shutil.copy(p+'/'+list_p[i], chiffon+'/'+list_p[i])
            elif b == '우븐':
                shutil.copy(p+'/'+list_p[i], woven+'/'+list_p[i])    


    elif data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['하의'][0].get('소재'):
        a=str(data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['하의'][0]['소재'])
        b=a[2:-2]
        if os.path.exists(p+'/'+list_j[i][:-5]+'.jpg') == 1:
            if b == '퍼':
                shutil.copy(p+'/'+list_p[i], fur+'/'+list_p[i])
            elif b == '무스탕':
                shutil.copy(p+'/'+list_p[i], mustang+'/'+list_p[i])
            elif b == '스웨이드':
                shutil.copy(p+'/'+list_p[i], suede+'/'+list_p[i])
            elif b == '앙고라':
                shutil.copy(p+'/'+list_p[i], angora+'/'+list_p[i])
            elif b == '코듀로이':
                shutil.copy(p+'/'+list_p[i], corduroy+'/'+list_p[i])
            elif b == '시퀸/글리터':
                shutil.copy(p+'/'+list_p[i], sequin+'/'+list_p[i])
            elif b == '데님':
                shutil.copy(p+'/'+list_p[i], denim+'/'+list_p[i])
            elif b == '저지':
                shutil.copy(p+'/'+list_p[i], jersey+'/'+list_p[i])
            elif b == '트위드':
                shutil.copy(p+'/'+list_p[i], tweed+'/'+list_p[i])
            elif b == '벨벳':
                shutil.copy(p+'/'+list_p[i], velvet+'/'+list_p[i])
            elif b == '비닐/PVC':
                shutil.copy(p+'/'+list_p[i], vinyl+'/'+list_p[i])
            elif b == '울/캐시미어':
                shutil.copy(p+'/'+list_p[i], wool+'/'+list_p[i])
            elif b == '합성섬유':
                shutil.copy(p+'/'+list_p[i], synthetic+'/'+list_p[i])
            elif b == '니트':
                shutil.copy(p+'/'+list_p[i], knit+'/'+list_p[i])
            elif b == '레이스':
                shutil.copy(p+'/'+list_p[i], lace+'/'+list_p[i])
            elif b == '린넨':
                shutil.copy(p+'/'+list_p[i], linen+'/'+list_p[i])
            elif b == '메시':
                shutil.copy(p+'/'+list_p[i], mesh+'/'+list_p[i])
            elif b == '플리스':
                shutil.copy(p+'/'+list_p[i], fleece+'/'+list_p[i])
            elif b == '네오프렌':
                shutil.copy(p+'/'+list_p[i], neoprene+'/'+list_p[i])
            elif b == '실크':
                shutil.copy(p+'/'+list_p[i], silk+'/'+list_p[i])
            elif b == '스판덱스':
                shutil.copy(p+'/'+list_p[i], spandex+'/'+list_p[i])
            elif b == '자카드':
                shutil.copy(p+'/'+list_p[i], jacquard+'/'+list_p[i])
            elif b == '가죽':
                shutil.copy(p+'/'+list_p[i], leather+'/'+list_p[i])
            elif b == '면':
                shutil.copy(p+'/'+list_p[i], cotton+'/'+list_p[i])
            elif b == '시폰':
                shutil.copy(p+'/'+list_p[i], chiffon+'/'+list_p[i])
            elif b == '우븐':
                shutil.copy(p+'/'+list_p[i], woven+'/'+list_p[i]) 


    elif data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['원피스'][0].get('소재'):
        a=str(data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['원피스'][0]['소재'])
        b=a[2:-2]
        if os.path.exists(p+'/'+list_j[i][:-5]+'.jpg') == 1:
            if b == '퍼':
                shutil.copy(p+'/'+list_p[i], fur+'/'+list_p[i])
            elif b == '무스탕':
                shutil.copy(p+'/'+list_p[i], mustang+'/'+list_p[i])
            elif b == '스웨이드':
                shutil.copy(p+'/'+list_p[i], suede+'/'+list_p[i])
            elif b == '앙고라':
                shutil.copy(p+'/'+list_p[i], angora+'/'+list_p[i])
            elif b == '코듀로이':
                shutil.copy(p+'/'+list_p[i], corduroy+'/'+list_p[i])
            elif b == '시퀸/글리터':
                shutil.copy(p+'/'+list_p[i], sequin+'/'+list_p[i])
            elif b == '데님':
                shutil.copy(p+'/'+list_p[i], denim+'/'+list_p[i])
            elif b == '저지':
                shutil.copy(p+'/'+list_p[i], jersey+'/'+list_p[i])
            elif b == '트위드':
                shutil.copy(p+'/'+list_p[i], tweed+'/'+list_p[i])
            elif b == '벨벳':
                shutil.copy(p+'/'+list_p[i], velvet+'/'+list_p[i])
            elif b == '비닐/PVC':
                shutil.copy(p+'/'+list_p[i], vinyl+'/'+list_p[i])
            elif b == '울/캐시미어':
                shutil.copy(p+'/'+list_p[i], wool+'/'+list_p[i])
            elif b == '합성섬유':
                shutil.copy(p+'/'+list_p[i], synthetic+'/'+list_p[i])
            elif b == '니트':
                shutil.copy(p+'/'+list_p[i], knit+'/'+list_p[i])
            elif b == '레이스':
                shutil.copy(p+'/'+list_p[i], lace+'/'+list_p[i])
            elif b == '린넨':
                shutil.copy(p+'/'+list_p[i], linen+'/'+list_p[i])
            elif b == '메시':
                shutil.copy(p+'/'+list_p[i], mesh+'/'+list_p[i])
            elif b == '플리스':
                shutil.copy(p+'/'+list_p[i], fleece+'/'+list_p[i])
            elif b == '네오프렌':
                shutil.copy(p+'/'+list_p[i], neoprene+'/'+list_p[i])
            elif b == '실크':
                shutil.copy(p+'/'+list_p[i], silk+'/'+list_p[i])
            elif b == '스판덱스':
                shutil.copy(p+'/'+list_p[i], spandex+'/'+list_p[i])
            elif b == '자카드':
                shutil.copy(p+'/'+list_p[i], jacquard+'/'+list_p[i])
            elif b == '가죽':
                shutil.copy(p+'/'+list_p[i], leather+'/'+list_p[i])
            elif b == '면':
                shutil.copy(p+'/'+list_p[i], cotton+'/'+list_p[i])
            elif b == '시폰':
                shutil.copy(p+'/'+list_p[i], chiffon+'/'+list_p[i])
            elif b == '우븐':
                shutil.copy(p+'/'+list_p[i], woven+'/'+list_p[i])      


    elif data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['상의'][0].get('소재'):
        a=str(data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['상의'][0]['소재'])
        b=a[2:-2]
        if os.path.exists(p+'/'+list_j[i][:-5]+'.jpg') == 1:
            if b == '퍼':
                shutil.copy(p+'/'+list_p[i], fur+'/'+list_p[i])
            elif b == '무스탕':
                shutil.copy(p+'/'+list_p[i], mustang+'/'+list_p[i])
            elif b == '스웨이드':
                shutil.copy(p+'/'+list_p[i], suede+'/'+list_p[i])
            elif b == '앙고라':
                shutil.copy(p+'/'+list_p[i], angora+'/'+list_p[i])
            elif b == '코듀로이':
                shutil.copy(p+'/'+list_p[i], corduroy+'/'+list_p[i])
            elif b == '시퀸/글리터':
                shutil.copy(p+'/'+list_p[i], sequin+'/'+list_p[i])
            elif b == '데님':
                shutil.copy(p+'/'+list_p[i], denim+'/'+list_p[i])
            elif b == '저지':
                shutil.copy(p+'/'+list_p[i], jersey+'/'+list_p[i])
            elif b == '트위드':
                shutil.copy(p+'/'+list_p[i], tweed+'/'+list_p[i])
            elif b == '벨벳':
                shutil.copy(p+'/'+list_p[i], velvet+'/'+list_p[i])
            elif b == '비닐/PVC':
                shutil.copy(p+'/'+list_p[i], vinyl+'/'+list_p[i])
            elif b == '울/캐시미어':
                shutil.copy(p+'/'+list_p[i], wool+'/'+list_p[i])
            elif b == '합성섬유':
                shutil.copy(p+'/'+list_p[i], synthetic+'/'+list_p[i])
            elif b == '니트':
                shutil.copy(p+'/'+list_p[i], knit+'/'+list_p[i])
            elif b == '레이스':
                shutil.copy(p+'/'+list_p[i], lace+'/'+list_p[i])
            elif b == '린넨':
                shutil.copy(p+'/'+list_p[i], linen+'/'+list_p[i])
            elif b == '메시':
                shutil.copy(p+'/'+list_p[i], mesh+'/'+list_p[i])
            elif b == '플리스':
                shutil.copy(p+'/'+list_p[i], fleece+'/'+list_p[i])
            elif b == '네오프렌':
                shutil.copy(p+'/'+list_p[i], neoprene+'/'+list_p[i])
            elif b == '실크':
                shutil.copy(p+'/'+list_p[i], silk+'/'+list_p[i])
            elif b == '스판덱스':
                shutil.copy(p+'/'+list_p[i], spandex+'/'+list_p[i])
            elif b == '자카드':
                shutil.copy(p+'/'+list_p[i], jacquard+'/'+list_p[i])
            elif b == '가죽':
                shutil.copy(p+'/'+list_p[i], leather+'/'+list_p[i])
            elif b == '면':
                shutil.copy(p+'/'+list_p[i], cotton+'/'+list_p[i])
            elif b == '시폰':
                shutil.copy(p+'/'+list_p[i], chiffon+'/'+list_p[i])
            elif b == '우븐':
                shutil.copy(p+'/'+list_p[i], woven+'/'+list_p[i])
