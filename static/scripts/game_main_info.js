console.log("Sanity check from room.js.");

const game_id = JSON.parse(document.getElementById('gameID').textContent);

let wishlistButton = document.getElementById("wishlist");
let ignoreButton = document.getElementById("ignore");

function wishlist() {
    gameSocket.send(
        JSON.stringify(
            {"message": 'add_to_wishlist'}
        )
    );
};

function ignore() {
    gameSocket.send(
        JSON.stringify(
            {"message": 'add_to_ignorelist'}
        )
    );
};
wishlistButton.addEventListener('click',wishlist)
ignoreButton.addEventListener('click',ignore)

let reviewInput = document.getElementById('review-text')
let reviewButtonYes = document.getElementById('review-req-yes')
let reviewButtonNo = document.getElementById('review-req-no')
let reviewValue = null
let reviewSubmitButton = document.getElementById('review-submit')

function reviewValueYes(){
    reviewValue = 1
}
function reviewValueNo(){
    reviewValue = 0
}
function reviewSubmit(){
    console.log(reviewInput.value)
    gameSocket.send(
        JSON.stringify(
            {
                "message": 'add_review',
                'text':reviewInput.value,
                'value':reviewValue
            }
        )
    );
}
reviewButtonYes.addEventListener('click',reviewValueYes)
reviewButtonNo.addEventListener('click',reviewValueNo)
reviewSubmitButton.addEventListener('click',reviewSubmit)
let gameSocket = null;

function connect() {
    gameSocket = new WebSocket("ws://" + window.location.host + "/ws/game/" + game_id + "/");

    gameSocket.onopen = function(e) {
        console.log("Successfully connected to the WebSocket.");
    }

    gameSocket.onclose = function(e) {
        console.log("WebSocket connection closed unexpectedly. Trying to reconnect in 2s...");
        setTimeout(function() {
            console.log("Reconnecting...");
            connect();
        }, 2000);
    };

    gameSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        // console.log(data);

        switch (data.type) {
            case "add_to_wishlist":
                wishlistButton.innerHTML = 'Remove from wishlist'
                break;
            case "remove_from_wishlist":
                wishlistButton.innerHTML = 'Add to wishlist'
                break;
            case 'add_to_ignorelist':
                ignoreButton.innerHTML = 'Remove from ignored games'
                break;
            case 'remove_from_ignorelist':
                ignoreButton.innerHTML = 'Ignore'
                break;
            default:
                console.error("Unknown message type!");
                break;
        }

    };

    gameSocket.onerror = function(err) {
        console.log("WebSocket encountered an error: " + err.message);
        console.log("Closing the socket.");
        gameSocket.close();
    }
}

connect();