<script setup>
// import { ref } from "vue";
defineProps({
  msg: String,
});
</script>

<template>
  <div class="h-screen bg-cyan-800 overflow-y-auto">
    <nav class="bg-sky-950">
      <div
        class="max-w-screen-xl drop-shadow-lg flex flex-wrap items-center justify-between mx-auto p-4"
      >
        <h1 class="font-sans text-xl text-white ">Analyzer</h1>
      </div>
    </nav>
    <div class="grid grid-cols-6 gap-y-6 pb-5 font-sans">
      <div class="bg-white rounded-lg shadow-2xl min-h-[50px] row-start-3 col-start-2 col-span-4">
          <h1 class="pt-4 pl-4 pb-4 text-lg">Keypoints</h1>
          <h2 class="pl-4 pb-4">Infomation</h2>
      </div>
      <div class="bg-white rounded-lg shadow-2xl min-h-[50px] row-start-4 col-start-2 col-span-4">
          <h1 class="pt-4 pl-4 pb-4 text-lg">Analyze</h1>
          <h2 class="pl-4 pb-4">Infomation</h2>
      </div>
      <div class="bg-white rounded-lg shadow-2xl min-h-[50px] row-start-5 col-start-2 col-span-4">
          <h1 class="pt-4 pl-4 pb-4 text-lg">Sentiment Analysis</h1>
          <div class="pl-4 pb-4 grid grid-cols-3 gap-x-3">
            <h2>Positive tone</h2>
            <h2 class = "pl-5">Neutral tone</h2>
            <h2 class = "pl-5">Negative tone</h2>
          </div>
      </div>
      <div class="bg-white rounded-lg shadow-2xl min-h-[50px] row-start-6 col-start-2 col-span-4">
          <h1 class="pt-4 pl-4 pb-4 text-lg">Reliability score</h1>
          <h2 class="pl-4 pb-4">Infomation</h2>
      </div>
      <div class="bg-white rounded-lg shadow-2xl min-h-[50px] row-start-7 col-start-2 col-span-4">
          <h1 class="pt-4 pl-4 text-lg">Feedback</h1>
          <div class="grid grid-rows-2">
            <div class="pt-3 grid grid-cols-2">
              <h2 class ="pl-4">Good</h2>
              <h2>Bad</h2>
            </div>
          </div>
          <div class="pl-4 pb-4 pr-4">
              <h2 class="pb-3">Textual Feedback:</h2>
              <input type="text" id="default-input" class="w-100 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
              <div class="pt-4 text-right">
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
              Button
              </button>
              </div>
              
            </div>
          
      </div>
      
    </div>

    <!-- <div class="row-start-2 col-start-2 row-span-2 col-span-2 bg-white rounded-lg m-h-64 p-2 transform hover:translate-y-2 hover:shadow-xl transition duration-300">
      <h1>Hello</h1> 
    </div> -->

  </div>
</template>



<style scoped>
html {
  font-family: "Inter", system-ui, sans-serif;
}
</style>
