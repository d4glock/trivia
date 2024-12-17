class GameManager {
    constructor() {
        this.gameId = null;
        this.questionNumber = 0;
        this.totalQuestions = 0;
        this.score = 0;
        this.setupEventListeners();
    }

    setupEventListeners() {
        const startButton = document.getElementById('start-game');
        if (startButton) {
            startButton.addEventListener('click', () => this.startGame());
        }

        const answerForm = document.getElementById('answer-form');
        if (answerForm) {
            answerForm.addEventListener('submit', (e) => {
                e.preventDefault();
                this.submitAnswer();
            });
        }
    }

    getAuthToken() {
        return localStorage.getItem('authToken');
    }

    getCsrfToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }

    async startGame() {
        try {
            const response = await fetch('/api/games/start_game/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCsrfToken(),
                    'Authorization': `Token ${this.getAuthToken()}`
                }
            });
    
            if (!response.ok) {
                throw new Error('Error al iniciar el juego');
            }
    
            const data = await response.json();
            this.gameId = data.game_id;
            this.questionNumber = 1;
            this.totalQuestions = 10;
            this.score = 0;
            this.displayQuestion(data.question);
            this.updateGameStatus();
        } catch (error) {
            this.showMessage('Error al iniciar el juego: ' + error.message, 'error');
        }
    }

    displayQuestion(question) {
        const questionContainer = document.getElementById('question-container');
        const answerContainer = document.getElementById('answer-container');
        const answerForm = document.getElementById('answer-form');

        questionContainer.innerHTML = `
            <h3>Pregunta ${this.questionNumber} de ${this.totalQuestions}</h3>
            <p>${question.text}</p>
        `;

        answerContainer.innerHTML = question.options.map(option => `
            <div class="form-check">
                <input class="form-check-input" type="radio" name="answer" 
                       id="answer${option.id}" value="${option.text}">
                <label class="form-check-label" for="answer${option.id}">
                    ${option.text}
                </label>
            </div>
        `).join('');

        // Mostrar el formulario
        answerForm.style.display = 'block';
    }

    async submitAnswer() {
        const selectedAnswer = document.querySelector('input[name="answer"]:checked');
        if (!selectedAnswer) {
            this.showMessage('Por favor selecciona una respuesta', 'warning');
            return;
        }
    
        const requestData = {
            game_id: this.gameId,
            answer_text: selectedAnswer.value
        };
    
        console.log('Enviando datos:', requestData); // Para debugging
    
        try {
            const response = await fetch('/api/games/submit-answer/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCsrfToken(),
                    'Authorization': `Token ${this.getAuthToken()}`
                },
                body: JSON.stringify(requestData)
            });
    
            console.log('Status:', response.status); // Para debugging
    
            if (!response.ok) {
                const errorData = await response.json();
                console.error('Error response:', errorData); // Para debugging
                throw new Error(errorData.error || `Error ${response.status}: ${response.statusText}`);
            }
    
            const data = await response.json();
            console.log('Respuesta exitosa:', data); // Para debugging
            this.handleAnswerResponse(data);
        } catch (error) {
            console.error('Error completo:', error); // Para debugging
            this.showMessage(`Error al enviar la respuesta: ${error.message}`, 'error');
        }
    }

    handleAnswerResponse(data) {
        this.score = data.score;
        this.questionNumber++;

        if (data.is_correct) {
            this.showMessage('¡Respuesta correcta!', 'success');
        } else {
            this.showMessage('Respuesta incorrecta', 'error');
        }

        if (data.game_over) {
            this.showGameOver();
        } else {
            this.displayQuestion(data.next_question);
        }
        this.updateGameStatus();
    }

    updateGameStatus() {
        const statusContainer = document.getElementById('game-status');
        if (statusContainer) {
            statusContainer.innerHTML = `
                <p>Pregunta: ${this.questionNumber}/${this.totalQuestions}</p>
                <p>Puntaje: ${this.score}</p>
            `;
        }
    }

    showGameOver() {
        const gameContainer = document.getElementById('game-container');
        gameContainer.innerHTML = `
            <h2>¡Juego terminado!</h2>
            <p>Tu puntaje final es: ${this.score}</p>
            <button class="btn btn-primary" onclick="location.reload()">Jugar de nuevo</button>
        `;
    }

    showMessage(message, type) {
        const alertContainer = document.getElementById('alert-container');
        alertContainer.innerHTML = `
            <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        `;
    }
}

// Inicializar el juego cuando el DOM esté cargado
document.addEventListener('DOMContentLoaded', () => {
    new GameManager();
});