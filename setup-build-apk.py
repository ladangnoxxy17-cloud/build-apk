<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic-Tac-Toe 12 Kolom</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
            padding: 20px;
        }

        .container {
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            padding: 30px;
            max-width: 600px;
            width: 100%;
            text-align: center;
            animation: fadeIn 0.8s ease-out;
        }

        h1 {
            color: #333;
            margin-bottom: 20px;
            font-size: 2.5rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }

        .status {
            font-size: 1.5rem;
            margin-bottom: 20px;
            padding: 10px;
            border-radius: 10px;
            background-color: #f8f9fa;
            transition: all 0.3s ease;
        }

        .board {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            grid-gap: 10px;
            margin: 20px auto;
            max-width: 400px;
        }

        .cell {
            background-color: #fff;
            border: none;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            aspect-ratio: 1/1;
            font-size: 2rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .cell:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            background-color: #f0f0f0;
        }

        .cell.x {
            color: #e74c3c;
        }

        .cell.o {
            color: #3498db;
        }

        .controls {
            margin-top: 20px;
            display: flex;
            justify-content: center;
            gap: 15px;
        }

        button {
            background: linear-gradient(to right, #6a11cb, #2575fc);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 50px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }

        button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
        }

        button:active {
            transform: translateY(1px);
        }

        .winning-cell {
            animation: pulse 1s infinite;
            background-color: #2ecc71;
            color: white;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        @keyframes bounceIn {
            0% { transform: scale(0.3); opacity: 0; }
            50% { transform: scale(1.05); }
            70% { transform: scale(0.9); }
            100% { transform: scale(1); opacity: 1; }
        }

        .player-info {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .player {
            padding: 10px 20px;
            border-radius: 10px;
            font-weight: bold;
            transition: all 0.3s ease;
        }

        .player.active {
            background-color: #3498db;
            color: white;
            box-shadow: 0 4px 10px rgba(52, 152, 219, 0.4);
        }

        .player.x {
            color: #e74c3c;
        }

        .player.o {
            color: #3498db;
        }

        .score {
            font-size: 1.2rem;
            margin-top: 10px;
            font-weight: bold;
        }

        .message {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 20px 40px;
            border-radius: 10px;
            font-size: 2rem;
            z-index: 100;
            animation: bounceIn 0.5s;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Tic-Tac-Toe 12 Kolom</h1>
        
        <div class="player-info">
            <div class="player x active" id="playerX">Pemain X</div>
            <div class="player o" id="playerO">Pemain O</div>
        </div>
        
        <div class="status" id="status">Giliran Pemain X</div>
        
        <div class="board" id="board">
            <!-- Sel-sel papan permainan akan dibuat dengan JavaScript -->
        </div>
        
        <div class="score">
            Skor: <span id="scoreX">0</span> - <span id="scoreO">0</span>
        </div>
        
        <div class="controls">
            <button id="reset">Mulai Ulang Permainan</button>
            <button id="newGame">Permainan Baru</button>
        </div>
    </div>

    <div class="message" id="message"></div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Elemen DOM
            const boardElement = document.getElementById('board');
            const statusElement = document.getElementById('status');
            const resetButton = document.getElementById('reset');
            const newGameButton = document.getElementById('newGame');
            const playerXElement = document.getElementById('playerX');
            const playerOElement = document.getElementById('playerO');
            const scoreXElement = document.getElementById('scoreX');
            const scoreOElement = document.getElementById('scoreO');
            const messageElement = document.getElementById('message');
            
            // State permainan
            let board = Array(12).fill('');
            let currentPlayer = 'X';
            let gameActive = true;
            let scores = { X: 0, O: 0 };
            
            // Kombinasi pemenang untuk papan 3x4
            const winningConditions = [
                // Baris horizontal
                [0, 1, 2], [1, 2, 3],
                [4, 5, 6], [5, 6, 7],
                [8, 9, 10], [9, 10, 11],
                // Kolom vertikal
                [0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11],
                // Diagonal (kiri ke kanan)
                [0, 5, 10], [1, 6, 11],
                // Diagonal (kanan ke kiri)
                [2, 5, 8], [3, 6, 9]
            ];
            
            // Inisialisasi papan permainan
            function initializeBoard() {
                boardElement.innerHTML = '';
                for (let i = 0; i < 12; i++) {
                    const cell = document.createElement('button');
                    cell.classList.add('cell');
                    cell.setAttribute('data-index', i);
                    cell.addEventListener('click', () => cellClicked(i));
                    boardElement.appendChild(cell);
                }
            }
            
            // Fungsi ketika sel diklik
            function cellClicked(index) {
                if (board[index] !== '' || !gameActive) return;
                
                // Update papan dan tampilan
                board[index] = currentPlayer;
                const cell = document.querySelector(`[data-index="${index}"]`);
                cell.textContent = currentPlayer;
                cell.classList.add(currentPlayer.toLowerCase());
                
                // Animasi untuk sel yang baru diisi
                cell.style.animation = 'bounceIn 0.5s';
                setTimeout(() => {
                    cell.style.animation = '';
                }, 500);
                
                // Periksa apakah ada pemenang
                if (checkWinner()) {
                    gameActive = false;
                    scores[currentPlayer]++;
                    updateScore();
                    showMessage(`Pemain ${currentPlayer} Menang!`);
                    return;
                }
                
                // Periksa apakah seri
                if (isDraw()) {
                    gameActive = false;
                    showMessage("Permainan Seri!");
                    return;
                }
                
                // Ganti pemain
                currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
                updateStatus();
            }
            
            // Periksa apakah ada pemenang
            function checkWinner() {
                for (let condition of winningConditions) {
                    const [a, b, c] = condition;
                    if (board[a] && board[a] === board[b] && board[a] === board[c]) {
                        // Tandai sel pemenang
                        condition.forEach(index => {
                            document.querySelector(`[data-index="${index}"]`).classList.add('winning-cell');
                        });
                        return true;
                    }
                }
                return false;
            }
            
            // Periksa apakah permainan seri
            function isDraw() {
                return board.every(cell => cell !== '');
            }
            
            // Update status permainan
            function updateStatus() {
                statusElement.textContent = `Giliran Pemain ${currentPlayer}`;
                
                // Update tampilan pemain aktif
                if (currentPlayer === 'X') {
                    playerXElement.classList.add('active');
                    playerOElement.classList.remove('active');
                } else {
                    playerOElement.classList.add('active');
                    playerXElement.classList.remove('active');
                }
            }
            
            // Update skor
            function updateScore() {
                scoreXElement.textContent = scores.X;
                scoreOElement.textContent = scores.O;
            }
            
            // Tampilkan pesan kemenangan/seri
            function showMessage(msg) {
                messageElement.textContent = msg;
                messageElement.style.display = 'block';
                setTimeout(() => {
                    messageElement.style.display = 'none';
                }, 2000);
            }
            
            // Reset permainan (tetap simpan skor)
            function resetGame() {
                board = Array(12).fill('');
                gameActive = true;
                currentPlayer = 'X';
                initializeBoard();
                updateStatus();
            }
            
            // Permainan baru (reset skor juga)
            function newGame() {
                scores = { X: 0, O: 0 };
                updateScore();
                resetGame();
            }
            
            // Event listeners
            resetButton.addEventListener('click', resetGame);
            newGameButton.addEventListener('click', newGame);
            
            // Inisialisasi
            initializeBoard();
            updateStatus();
        });
    </script>
</body>
</html>
