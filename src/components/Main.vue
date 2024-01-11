<script setup>
import { ref } from "vue";
import { defineProps } from "vue";
import axios from "axios";

const text = ref("Unknown");
let inputText = ref("Text to analyse");
let keys = ref("Key points");
let analyze = ref("Analyze");
let sen_analyze = ref("Sentiment Analysis");
let reliability = ref("Reliability score");
let feedback = ref("Feedback"); //send when user click button


function send_user_input(input){
  const path = "http://127.0.0.1:5000/retrieve-data"; 
  axios.post(path, text).then((res) => {
    console.log(res.data);
  })
}

function send_input() {
  const path = "";
  axios.post(path, input_text).then((res) => {
    console.log(res.data);
    // keys = res.data
  });
}

function handleHighlight() {
  const selectedText = window.getSelection().toString();
  inputText.value = selectedText;
}
</script>

<template>
  <div class="h-screen bg-cyan-800 overflow-y-auto">
    <nav class="bg-sky-950">
      <div
        class="max-w-screen-xl drop-shadow-lg flex flex-wrap items-center justify-between mx-auto p-4"
      >
        <h1 class="font-sans text-xl text-white">Analyzer</h1>
      </div>
    </nav>
    <div class="grid grid-cols-6 gap-y-6 pb-5 font-sans">
      <!-- temporary  -->
      <div
        class="bg-white rounded-lg shadow-2xl min-h-[50px] row-start-3 col-start-2 col-span-4"
      >
        <div class="pt-4 pl-4 pb-4 pr-4">
          <h1 class="text-lg">Inputs</h1>
          <input
            v-model="text"
            type="input"
            id="user_input"
            class="w-100 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          />
        </div>
        <div class="pb-3 pr-4 text-right">
            <button
              type="submit"
              @click = "(event) => send_user_input(text)"
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            >
              Submit
            </button>
          </div>
      </div>

      <div
        class="bg-white rounded-lg shadow-2xl min-h-[50px] row-start-4 col-start-2 col-span-4"
      >
        <h1 class="pt-4 pl-4 pb-4 text-lg">Keypoints</h1>
        <h2 class="pl-4 pb-4">Information</h2>
      </div>
      <div
        class="bg-white rounded-lg shadow-2xl min-h-[50px] row-start-5 col-start-2 col-span-4"
      >
        <h1 class="pt-4 pl-4 pb-4 text-lg">Analyze</h1>
        <h2 class="pl-4 pb-4">Infomation</h2>
      </div>
      <div
        class="bg-white rounded-lg shadow-2xl min-h-[50px] row-start-6 col-start-2 col-span-4"
      >
        <h1 class="pt-4 pl-4 pb-4 text-lg">Sentiment Analysis</h1>
        <div class="pl-4 pb-4 grid grid-cols-3 gap-x-3">
          <h2>Positive tone</h2>
          <h2 class="pl-5">Neutral tone</h2>
          <h2 class="pl-5">Negative tone</h2>
        </div>
      </div>
      <div
        class="bg-white rounded-lg shadow-2xl min-h-[50px] row-start-7 col-start-2 col-span-4"
      >
        <h1 class="pt-4 pl-4 pb-4 text-lg">Reliability score</h1>
        <h2 class="pl-4 pb-4">Infomation</h2>
      </div>
      <div
        class="bg-white rounded-lg shadow-2xl min-h-[50px] row-start-8 col-start-2 col-span-4"
      >
        <h1 class="pt-4 pl-4 text-lg">Feedback</h1>
        <div class="grid grid-rows-2">
          <div class="pt-3 grid grid-cols-2">
            <h2 class="pl-4">Good</h2>
            <h2>Bad</h2>
          </div>
        </div>
        <div class="pl-4 pb-4 pr-4">
          <h2 class="pb-3">Textual Feedback:</h2>
          <input
            type="text"
            id="default-input"
            class="w-100 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          />
          <div class="pt-4 text-right">
            <button
              
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            >
              Button
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
html {
  font-family: "Inter", system-ui, sans-serif;
}
</style>
