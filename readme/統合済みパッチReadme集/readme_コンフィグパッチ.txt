﻿=================================================
触手宮Ver0.071用コンフィグパッチ

制作：
	イソツビ
	
最終更新：
	イソツビ	2012/09/25
	
ライセンス：
	改造・修正は自由にどうぞ
	※ライセンスの変更はダメ
	※改造や修正によりこのテキストでの説明と実際の仕様に差異が発生した場合は、
	説明の修正をお願いします。
	
=================================================

・パッチについて
このパッチはコンフィグの表示を少しだけ良くするものです
また、設定項目毎に関数分けしているので追加作業やメンテナンスが容易になると思われます。

・主な使用ファイル
SET_CONFIGURE.ERB

=================================================
　バリアント及びパッチ制作者様へ
=================================================

・コンフィグ項目について
このパッチではコンフィグの設定項目毎に関数分けをしており、関数名によって項目の位置関係を決定しています。
項目の関数名は SET_CONFIGURE の後ろにアンダーバー(_)と項目番号(1～99)が追加されたものとなっており、
階層が深いものほど後ろにアンダーバーと項目番号が追加されていきます

（例）
	@SET_CONFIGURE_1_1(ARG)
	@SET_CONFIGURE_1_1_1(ARG)
	@SET_CONFIGURE_1_1_1_1(ARG)

下の階層に移動するには選択時の処理の際（ARGが1のとき）にRESULT:0 に1を返せば移動します。
ただし、

	@SET_CONFIGURE_15(ARG)

で下の階層に移動した時は

	@SET_CONFIGURE_15_1(ARG)
	@SET_CONFIGURE_15_2(ARG)
	@SET_CONFIGURE_15_3(ARG)
	@SET_CONFIGURE_15_4(ARG)
		・
		・
		・
	@SET_CONFIGURE_15_99(ARG)

の関数が、

	@SET_CONFIGURE_21_34(ARG)

で下の階層に移動した時は

	@SET_CONFIGURE_21_34_1(ARG)
	@SET_CONFIGURE_21_34_2(ARG)
	@SET_CONFIGURE_21_34_3(ARG)
	@SET_CONFIGURE_21_34_4(ARG)
		・
		・
		・
	@SET_CONFIGURE_21_34_99(ARG)

という名前の関数が移動先の階層での表示対象となります


以上
=================================================
