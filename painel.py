import sys
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qdarktheme

class GitHubClone(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GitHub")
        self.setGeometry(100, 100, 1400, 900)
        self.setStyleSheet("background: #0d1117;")
        self.setup_ui()
        
    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # ========== NAVBAR ==========
        navbar = QWidget()
        navbar.setFixedHeight(60)
        navbar.setStyleSheet("""
            QWidget {
                background: #161b22;
                border-bottom: 1px solid #30363d;
            }
        """)
        nav_layout = QHBoxLayout(navbar)
        nav_layout.setContentsMargins(30, 0, 30, 0)
        
        # Logo
        logo = QLabel("🐙 GitHub")
        logo.setStyleSheet("""
            QLabel {
                color: #f0f6fc;
                font-size: 20px;
                font-weight: bold;
                padding: 0px 20px 0px 0px;
            }
        """)
        nav_layout.addWidget(logo)
        
        # Menu
        menus = ["Dashboard", "Repositories", "Projects", "Pull requests", "Issues"]
        for menu in menus:
            btn = QPushButton(menu)
            btn.setStyleSheet("""
                QPushButton {
                    color: #c9d1d9;
                    background: transparent;
                    border: none;
                    padding: 8px 16px;
                    font-size: 14px;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background: #21262d;
                    color: #f0f6fc;
                }
            """)
            nav_layout.addWidget(btn)
        
        # Barra de busca
        search = QLineEdit()
        search.setPlaceholderText("🔍 Search or jump to...")
        search.setStyleSheet("""
            QLineEdit {
                background: #0d1117;
                color: #c9d1d9;
                border: 1px solid #30363d;
                border-radius: 6px;
                padding: 6px 12px;
                min-width: 250px;
            }
            QLineEdit:focus {
                border-color: #58a6ff;
                outline: none;
            }
        """)
        nav_layout.addWidget(search)
        
        # Avatar
        avatar = QLabel("👤")
        avatar.setStyleSheet("""
            QLabel {
                background: #238636;
                border-radius: 20px;
                padding: 8px;
                min-width: 32px;
                min-height: 32px;
                color: white;
                font-size: 16px;
            }
        """)
        nav_layout.addWidget(avatar)
        
        nav_layout.addStretch()
        main_layout.addWidget(navbar)
        
        # ========== CONTEÚDO PRINCIPAL ==========
        content = QWidget()
        content_layout = QHBoxLayout(content)
        content_layout.setContentsMargins(30, 20, 30, 20)
        content_layout.setSpacing(20)
        
        # Sidebar esquerda
        sidebar = QWidget()
        sidebar.setFixedWidth(280)
        sidebar.setStyleSheet("background: transparent;")
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setSpacing(15)
        
        # Perfil
        perfil = QFrame()
        perfil.setStyleSheet("""
            QFrame {
                background: #161b22;
                border-radius: 12px;
                border: 1px solid #30363d;
                padding: 20px;
            }
        """)
        perfil_layout = QVBoxLayout(perfil)
        
        perfil_layout.addWidget(QLabel("👤 Seu Perfil"))
        
        nome = QLabel("Seu Nome")
        nome.setStyleSheet("font-size: 18px; font-weight: bold; color: #f0f6fc;")
        perfil_layout.addWidget(nome)
        
        username = QLabel("@seuusername")
        username.setStyleSheet("color: #8b949e; font-size: 14px;")
        perfil_layout.addWidget(username)
        
        desc = QLabel("Desenvolvedor Full Stack • 5 seguidores")
        desc.setStyleSheet("color: #c9d1d9; font-size: 13px;")
        perfil_layout.addWidget(desc)
        
        perfil_layout.addWidget(QLabel("📍 Brasil"))
        
        sidebar_layout.addWidget(perfil)
        
        # Stats
        stats = QFrame()
        stats.setStyleSheet("""
            QFrame {
                background: #161b22;
                border-radius: 12px;
                border: 1px solid #30363d;
                padding: 15px;
            }
        """)
        stats_layout = QVBoxLayout(stats)
        
        stats_data = [
            ("📚 Repositórios", "0"),
            ("🌟 Estrelas", "0"),
            ("👥 Seguidores", "0"),
            ("📌 Seguindo", "0"),
        ]
        
        for label, value in stats_data:
            item = QWidget()
            item_layout = QHBoxLayout(item)
            item_layout.setContentsMargins(0, 5, 0, 5)
            
            lbl = QLabel(label)
            lbl.setStyleSheet("color: #8b949e; font-size: 13px;")
            
            val = QLabel(value)
            val.setStyleSheet("color: #f0f6fc; font-weight: bold; font-size: 14px;")
            val.setAlignment(Qt.AlignRight)
            
            item_layout.addWidget(lbl)
            item_layout.addWidget(val)
            stats_layout.addWidget(item)
        
        sidebar_layout.addWidget(stats)
        
        # Repositórios recentes
        recentes = QFrame()
        recentes.setStyleSheet("""
            QFrame {
                background: #161b22;
                border-radius: 12px;
                border: 1px solid #30363d;
                padding: 15px;
            }
        """)
        recentes_layout = QVBoxLayout(recentes)
        
        titulo = QLabel("📁 Repositórios Recentes")
        titulo.setStyleSheet("color: #f0f6fc; font-weight: bold; font-size: 14px;")
        recentes_layout.addWidget(titulo)
        
        repos_exemplo = [
            ("projeto-awesome", "Python", "10⭐"),
            ("api-gateway", "Go", "5⭐"),
            ("frontend-app", "React", "3⭐"),
        ]
        
        for nome, lang, stars in repos_exemplo:
            repo_item = QPushButton(f"📂 {nome}  •  {lang}  {stars}")
            repo_item.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    border: none;
                    text-align: left;
                    padding: 8px 5px;
                    color: #c9d1d9;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background: #21262d;
                }
            """)
            recentes_layout.addWidget(repo_item)
        
        sidebar_layout.addWidget(recentes)
        sidebar_layout.addStretch()
        
        content_layout.addWidget(sidebar)
        
        # ========== FEED PRINCIPAL ==========
        feed = QWidget()
        feed_layout = QVBoxLayout(feed)
        feed_layout.setSpacing(15)
        
        # Abas
        tabs = QWidget()
        tabs.setStyleSheet("""
            QWidget {
                background: #161b22;
                border-radius: 12px;
                border: 1px solid #30363d;
            }
        """)
        tabs_layout = QHBoxLayout(tabs)
        tabs_layout.setContentsMargins(5, 5, 5, 5)
        
        tab_btns = ["📊 Feed", "📝 Pull Requests", "🐛 Issues", "⭐ Stars"]
        for tab in tab_btns:
            btn = QPushButton(tab)
            btn.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    border: none;
                    padding: 8px 16px;
                    color: #8b949e;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background: #21262d;
                    color: #f0f6fc;
                }
            """)
            tabs_layout.addWidget(btn)
        
        feed_layout.addWidget(tabs)
        
        # Cards de atividade
        for i in range(3):
            card = QFrame()
            card.setStyleSheet("""
                QFrame {
                    background: #161b22;
                    border-radius: 12px;
                    border: 1px solid #30363d;
                    padding: 20px;
                }
            """)
            card_layout = QVBoxLayout(card)
            
            # Cabeçalho do card
            cabecalho = QLabel("🌟 user/repo • 2 horas atrás")
            cabecalho.setStyleSheet("color: #8b949e; font-size: 13px;")
            card_layout.addWidget(cabecalho)
            
            # Título
            titulo_card = QLabel("Atualização importante no projeto")
            titulo_card.setStyleSheet("color: #f0f6fc; font-size: 16px; font-weight: bold;")
            card_layout.addWidget(titulo_card)
            
            # Descrição
            desc_card = QLabel("Adicionada nova funcionalidade de autenticação com OAuth2 e melhorias no sistema de cache...")
            desc_card.setStyleSheet("color: #c9d1d9; font-size: 14px;")
            desc_card.setWordWrap(True)
            card_layout.addWidget(desc_card)
            
            # Rodapé com ações
            acoes = QWidget()
            acoes_layout = QHBoxLayout(acoes)
            acoes_layout.setContentsMargins(0, 10, 0, 0)
            
            botoes = ["👍 15", "💬 3", "🔗"]
            for texto in botoes:
                btn_acao = QPushButton(texto)
                btn_acao.setStyleSheet("""
                    QPushButton {
                        background: transparent;
                        border: none;
                        color: #8b949e;
                        padding: 0px 15px 0px 0px;
                    }
                    QPushButton:hover {
                        color: #f0f6fc;
                    }
                """)
                acoes_layout.addWidget(btn_acao)
            
            acoes_layout.addStretch()
            card_layout.addWidget(acoes)
            
            feed_layout.addWidget(card)
        
        feed_layout.addStretch()
        content_layout.addWidget(feed)
        
        main_layout.addWidget(content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("dark")
    window = GitHubClone()
    window.show()
    sys.exit(app.exec_())
