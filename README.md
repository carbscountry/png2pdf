# 使い方
## 前準備
- 「設定」 => 「セキュリティとプライバシー」 => 「アクセシビリティ」 => 「+」を押す => 「スクリプトエディタ」を追加
- 「設定」 => 「セキュリティとプライバシー」 => 「画面収録とシステムオーディオ録音」 => 「+」を押す => 「スクリプトエディタ」を追加
## スクリプトエディタ準備編
以下のスクリプトを編集してコピー.<br>
ページ数と保存フォルダ先、めくり方向をpdf化したい本によってを変更。

```
-- ページ数
set pages to 416
-- 対象アプリ
set target to "Kindle"
-- 保存フォルダ
set savepath to "~/git/png2pdf/<書籍名>"
set savepath to POSIX path of (savepath as string)
-- 開始ファイル番号
set spage to 1
-- めくり方向(1=左 2=右)
set pagedir to 1
-- ページめくりウエイト(秒)
set pausetime to 1.0
-- 切り抜きサイズ(中心から)
set cropx to 0
set cropy to 0
-- リサイズ横(切り抜く前のサイズ換算=画面横/切り抜き横*仕上がり横)
set resizew to 0

-- フォルダが存在しない場合は作成
do shell script "mkdir -p " & quoted form of savepath

if pagedir = 1 then
    set keychar to (ASCII character 28)
else
    set keychar to (ASCII character 29)
end if

if target is not "" then
    tell application target
        activate
    end tell
end if

delay pausetime

repeat with i from spage to pages
    if i < 10 then
        set dp to "00" & i
    else if i < 100 then
        set dp to "0" & i
    else
        set dp to i as string
    end if
    set spath to savepath & "p" & dp & ".png"
    do shell script "screencapture " & quoted form of spath
    if cropx is not 0 and cropy is not 0 then
        if resizew is not 0 then
            do shell script "sips -c " & cropy & " " & cropx & " --resampleWidth " & resizew & " " & quoted form of spath & " --out " & quoted form of spath
        else
            do shell script "sips -c " & cropy & " " & cropx & " " & quoted form of spath & " --out " & quoted form of spath
        end if
    end if
    tell application "System Events"
        keystroke keychar
    end tell
    delay pausetime
end repeat

activate

```
## スクリプトエディタ起動
- 1.上記の内容がコピーできていることを確認。pdf化したいkindle本をフルスクリーンで表示知っておく。（最初のページで）
- 2.スクリプトエディタ起動(cmd + shiftで検索バーを開いてスクリプトとうつと出てくるはず)
- 3.右下の新規作成を押す(できればcloneしたディレクトリ下で)
- 4.先程のコピーした内容を貼り付けて「▶」を押す。途中で中断したい場合は「■」を押す。
## スクショをマージしてpdfにする
- 0.pipが使える状態にしておく。
- 1.uvをダウンロード
- 2.``uv pip install -r pyproject.toml  ``を実行
- 3.``main.py``のdir_pathにスクショを保存したディレクトリを入れる
- 4.``uv run python main.py``