/* module for importing other js files */
function include(file) {
  const script = document.createElement('script');
  script.src = file;
  script.type = 'text/javascript';
  script.defer = true;

  document.getElementsByTagName('head').item(0).appendChild(script);
}

// Bot pop-up intro
document.addEventListener("DOMContentLoaded", () => {
  const elemsTap = document.querySelector(".tap-target");
  const instancesTap = M.TapTarget.init(elemsTap, {});
  instancesTap.open();
  setTimeout(() => {
    instancesTap.close();
  }, 55000);
});

/* import components */
include('./static/js/components/index.js');

// Function to display initial user message
// function displayInitialUserMessage() {
//   const userMessage = "Hello! How can I help you today?";
//   const messageContainer = document.createElement('div');
//   messageContainer.textContent = userMessage;
//   messageContainer.classList.add('user-message'); // Add a class for styling purposes

//   // Append the message to your chat container
//   // Replace 'chatContainer' with the id or class of your chat container
//   document.querySelector('#chats').appendChild(messageContainer);
// }

window.addEventListener('load', () => {
  // initialization
  $(document).ready(() => {
    // Bot pop-up intro
    $("div").removeClass("tap-target-origin");

    // drop down menu for close, restart conversation & clear the chats.
    $(".dropdown-trigger").dropdown();

    // initiate the modal for displaying the charts,
    // if you don't have charts, then you can comment the below line
    $(".modal").modal();

    // enable this if you have configured the bot to start the conversation.
    // showBotTyping();
    // $("#userInput").prop('disabled', true);

    // if you want the bot to start the conversation
    // customActionTrigger();

    // Display initial user message
    displayInitialUserMessage();
  });

  // Toggle the chatbot screen
  $("#profile_div").click(() => {
    $(".profile_div").toggle();
    $(".widget").toggle();
  });

  // clear function to clear the chat contents of the widget.
  $("#clear").click(() => {
    $(".chats").fadeOut("normal", () => {
      $(".chats").html("");
      $(".chats").fadeIn();
    });
  });

  // close function to close the widget.
  $("#close").click(() => {
    $(".profile_div").toggle();
    $(".widget").toggle();
    scrollToBottomOfResults();
  });
});
