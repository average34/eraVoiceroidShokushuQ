﻿
------------------------------------------------------------
	東方触手宮 膨乳病勝手に修正パッチ
	東方触手宮1.03.8で動作確認済
											作:ふぅりすと
------------------------------------------------------------

母乳製造装置状態のてゐちゃんが貧乳から一瞬で奇乳になった!?
急激な豊乳化もキライじゃないけど今はそうじゃない



■ パッチ内容
使い魔によって[母乳製造装置]を取得(他の方法で同素質取得も含)した場合、爆乳以外からの状態からでも一瞬で奇乳となる
違和感があるので爆乳未満の場合一段階ずつバストサイズが上昇するよう変更

バストサイズ変化を既存の関数で行う事によってバストサイズ変更後にキャラ別口上が呼び出されるようになる


■ 変更詳細
CHECK_GROW_BUST.ERB
	膨乳の処理を内部で行う方法からADD_BUST or SET_BUST関数で行う方法に変更

SYSTEM_MESSAGE_509_膨乳病.ERB
	バストサイズ変化の地の文表示を行わないように変更
		※ バストサイズ変化.ERB側で行うのが正しいと判断

SYSTEM_MESSAGE_510_バストサイズ変化.ERB
	コメント変更 ARG:4 変化理由に膨乳病 を追加

BUST_バストサイズ処理.ERB
	コメント追加 上記バストサイズ変化.ERBと同様の説明を
	SET_BUST関数内で CFLAG:506 母乳量の初期化を行うように
		※奇乳化進行中にバストサイズが変化した場合、メッセージ表示がおかしくなるのを防ぐ為
	
