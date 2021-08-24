const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

let field = [];
let mines_count = 0;
let mines_found = 0;

const CELL_SIZE = 40;
const MINES_MAX = 10;

function randomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
}

function initCanvas() {
        canvas.width = 800;
        canvas.height = 400;
};

function initField() {

        for (let i = 0; i < 10; i++) {
                field[i] = [];
                
        }

        for (let x = 0; x < 10; x++) {
                for (let y = 0; y < 10; y++) {
                        field[x][y] = 0;
                }
        }
}

function getMine(x, y) {
        if (x < 0 || x > 9 || y < 0 || y > 9) {
                return 0
        }
        if (field[x][y] == -1) {
                return 1
        }
        return 0
}

function createMines() {
        while(mines_count < MINES_MAX) {
                const mine_x = randomInt(0, 9);
                const mine_y = randomInt(0, 9);
                if(field[mine_x][mine_y] !== -1) {
                        field[mine_x][mine_y] = -1;
                        mines_count += 1;
                }
        }
}

function placeNums () {
        for (let x = 0; x < 9; x++) {
                for (let y = 0; y < 10; y++) {
                        if (field[x][y] == -1) {
                                continue
                        }
                        const around = getMine(x-1, y) + getMine(x-1, y-1) + getMine(x-1, y+1) + getMine(x, y+1) + getMine(x, y-1) + getMine(x+1, y-1) + getMine(x+1, y) + getMine(x+1, y+1);
                        field[x][y] = around;
                }
        }
}

function fillField() {
        createMines();
        placeNums();
}

function main() {
        initCanvas();

        mines_found = 0;
        mines_count = 0;
        field = [];

        initField();
        fillField();
}

main();