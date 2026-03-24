*This project has been created as part of the 42 curriculum by hwakatsu.*

# DataDeck

## Description / 説明

### English
DataDeck is a Python project about abstract programming patterns through a modular trading card game engine. Its goal is to practice abstract base classes, polymorphism, multiple inheritance, and interface composition by building a system where different card types can share common contracts while keeping their own behavior.

The repository is structured as a package-based progression:

- `ex0`: abstract card foundation with `Card` and `CreatureCard`
- `ex1`: concrete card types and deck management with `SpellCard`, `ArtifactCard`, and `Deck`
- `ex2`: multiple interface design with `Combatable`, `Magical`, and `EliteCard`
- `ex3`: engine architecture using Strategy and Abstract Factory patterns
- `ex4`: tournament system with ranking and match management

Based on the code in this repository, the project demonstrates:

- validation of card attributes such as cost, rarity, attack, health, and durability
- shared card behaviors through the abstract `Card` base class
- polymorphic deck handling for creatures, spells, and artifacts
- multiple inheritance for cards that can both fight and cast spells
- tournament ranking logic and leaderboard generation

### 日本語
DataDeck は、モジュール式のトレーディングカードゲームエンジンを題材に、抽象プログラミングパターンを学ぶ Python プロジェクトです。目的は、抽象基底クラス、ポリモーフィズム、多重継承、インターフェース合成を使って、共通の契約を保ちながら異なる振る舞いを持つカードシステムを構築することです。

このリポジトリは、パッケージ単位で段階的に構成されています。

- `ex0`: `Card` と `CreatureCard` による抽象カード基盤
- `ex1`: `SpellCard`、`ArtifactCard`、`Deck` による具体的カード型とデッキ管理
- `ex2`: `Combatable`、`Magical`、`EliteCard` による複数インターフェース設計
- `ex3`: Strategy パターンと Abstract Factory パターンを使ったゲームエンジン
- `ex4`: ランキングと対戦管理を備えたトーナメントシステム

このリポジトリの実装では、次の内容が確認できます。

- コスト、レアリティ、攻撃力、体力、耐久値などのカード属性検証
- 抽象基底クラス `Card` を通した共通カード動作の定義
- クリーチャー、スペル、アーティファクトを同じデッキで扱うポリモーフィズム
- 戦闘と魔法の両方を扱えるカードを作るための多重継承
- トーナメントにおけるレーティング更新とリーダーボード生成

## Instructions / 実行方法

### English

Requirements:

- Python 3.10 or later
- No external dependencies

This project is designed as Python packages. Run each exercise from the repository root:

```bash
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main
```

Optional lint check:

```bash
flake8 .
```

There is no installation or compilation step. Clone the repository and run the modules directly from the project root so that absolute imports such as `from ex0.Card import Card` work correctly.

### 日本語

必要環境:

- Python 3.10 以上
- 外部依存関係なし

このプロジェクトは Python パッケージ構成になっているため、リポジトリのルートから各 exercise を実行します。

```bash
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main
```

任意の lint チェック:

```bash
flake8 .
```

インストールやコンパイルは不要です。リポジトリを取得したら、`from ex0.Card import Card` のような絶対 import が正しく動くように、必ずプロジェクトルートから実行してください。

## Features / 主な内容

### English

- `Card` is implemented as an abstract base class with a required `play()` contract.
- `CreatureCard`, `SpellCard`, and `ArtifactCard` provide different concrete play behaviors.
- `Deck` manages mixed card types through a common `Card` interface.
- `EliteCard` combines combat and magic interfaces in one class.
- `GameEngine` coordinates a factory and a strategy to simulate turns.
- `TournamentPlatform` registers cards, creates matches, updates ratings, and builds a leaderboard.

### 日本語

- `Card` は抽象基底クラスとして実装され、`play()` の実装を必須にしています。
- `CreatureCard`、`SpellCard`、`ArtifactCard` はそれぞれ異なる具体的なプレイ動作を持ちます。
- `Deck` は共通の `Card` インターフェースを通して異種カードを管理します。
- `EliteCard` は戦闘インターフェースと魔法インターフェースを 1 つのクラスに統合しています。
- `GameEngine` は factory と strategy を組み合わせてターン進行をシミュレートします。
- `TournamentPlatform` はカード登録、対戦、レーティング更新、リーダーボード生成を行います。

## Project Structure / 構成

### English

- [`__init__.py`](/Users/hikaru/project/42/python7/__init__.py): root package marker required for absolute imports
- [`ex0`](/Users/hikaru/project/42/python7/ex0): foundation layer
- [`ex1`](/Users/hikaru/project/42/python7/ex1): deck builder layer
- [`ex2`](/Users/hikaru/project/42/python7/ex2): ability system layer
- [`ex3`](/Users/hikaru/project/42/python7/ex3): game engine layer
- [`ex4`](/Users/hikaru/project/42/python7/ex4): tournament platform layer

### 日本語

- [`__init__.py`](/Users/hikaru/project/42/python7/__init__.py): 絶対 import のために必要なルートパッケージマーカー
- [`ex0`](/Users/hikaru/project/42/python7/ex0): 基盤レイヤー
- [`ex1`](/Users/hikaru/project/42/python7/ex1): デッキ構築レイヤー
- [`ex2`](/Users/hikaru/project/42/python7/ex2): 能力システムレイヤー
- [`ex3`](/Users/hikaru/project/42/python7/ex3): ゲームエンジンレイヤー
- [`ex4`](/Users/hikaru/project/42/python7/ex4): トーナメントプラットフォームレイヤー

## Resources / 参考資料

### English

Classic references related to the topic:

- [Python Documentation: abc](https://docs.python.org/3/library/abc.html)
- [Python Documentation: enum](https://docs.python.org/3/library/enum.html)
- [Python Documentation: typing](https://docs.python.org/3/library/typing.html)
- [Python Documentation: random](https://docs.python.org/3/library/random.html)
- [Real Python: Inheritance and Composition](https://realpython.com/inheritance-composition-python/)
- [Refactoring Guru: Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)
- [Refactoring Guru: Strategy](https://refactoring.guru/design-patterns/strategy)
- [flake8 Documentation](https://flake8.pycqa.org/)

AI usage in this project:

- AI was used for documentation support and README writing.
- It was used to inspect the repository structure, summarize the implemented architecture, and produce bilingual English/Japanese explanations.
- The README content was aligned with the code in `ex0` through `ex4`, but the implementation itself should still be reviewed manually and fully understood for peer evaluation.

### 日本語

この課題に関連する代表的な参考資料:

- [Python Documentation: abc](https://docs.python.org/3/library/abc.html)
- [Python Documentation: enum](https://docs.python.org/3/library/enum.html)
- [Python Documentation: typing](https://docs.python.org/3/library/typing.html)
- [Python Documentation: random](https://docs.python.org/3/library/random.html)
- [Real Python: Inheritance and Composition](https://realpython.com/inheritance-composition-python/)
- [Refactoring Guru: Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)
- [Refactoring Guru: Strategy](https://refactoring.guru/design-patterns/strategy)
- [flake8 Documentation](https://flake8.pycqa.org/)

このプロジェクトにおける AI の利用:

- AI はドキュメント補助と README 作成に使用しました。
- リポジトリ構成の確認、実装済みアーキテクチャの要約、英語と日本語の説明文作成に利用しました。
- README の内容は `ex0` から `ex4` のコードを参照して整合させていますが、実装そのものは peer review に向けて自分で確認し、説明できる状態にしておく必要があります。

## Notes / 補足

### English
This project focuses on architecture rather than deep game balance. The main objective is to demonstrate clean abstract design, reusable contracts, and extensible card-system structure.

### 日本語
このプロジェクトはゲームバランスの作り込みよりもアーキテクチャ設計を重視しています。主目的は、明確な抽象設計、再利用可能な契約、拡張しやすいカードシステム構造を示すことです。
