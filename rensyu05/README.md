##　第5回
###　Pygameによるゲーム開発
####　３限
-Screenクラスを作る
　　-コンストラクタ（背景画像ファイル名，幅高さ，タイトル）
    　　-タイトルを設定する
            • 幅高さを指定して，スクリーン用のSurfaceを生成する
            • スクリーン用のSurfaceのrectを取得する
            • 背景画像用のSurfaceを生成する
        -インスタンス変数
            • int width：スクリーンの幅
            • int height：スクリーンの高さ
            • Surface disp：スクリーン用のSurface
            • Rect rect：dispのrectオブジェクト
            • Surface image：背景画像用のSurface
    -Birdクラスを作る
        -インスタンスメソッド：update(Screenオブジェクト)
            • キーの押下状態を取得する
            • 押下状態に応じてこうかとんを移動する
            • こうかとんの位置がScreenに収まっているかチェックする
-Bombクラスを作る
        -上記と大体同じ

#### 4限
    -Groupクラスを利用して爆弾を処理する記述を追加
　　　　　-spriteモジュールのgroupcollide関数を使用して衝突している爆弾数を求め一つでも衝突していたらMain関数からreturnする記述
#### 追加機能
- 画面にScoreを表示
- 爆弾の大きさを少しずつ大きくする

#### ToDo
- GameOver画面を表示