<template>
  <div class="container mx-auto p-4">
    <h1 class="text-4xl font-bold text-center mb-4 gradient-text">AI Color Scheme Generator</h1>
    <p class="text-center mb-4">Upload an image to generate a matching color palette.</p>

    <div class="flex justify-center items-center mb-4">
      <label class="block">
        <span class="sr-only">Choose profile photo</span>
        <input type="file" @change="uploadImage" class="file-input file-input-bordered w-full max-w-xs"/>
      </label>
    </div>

    <div class="card w-96 bg-base-100 shadow-xl mx-auto" v-if="imageData">
      <figure><img :src="imageData" alt="Color palette" /></figure>
      <div class="card-body">
        <div v-if="colors.length" class="flex justify-center items-center flex-wrap mb-4">
          <div v-for="(color, index) in colors" :key="index" 
               class="w-20 h-20 m-2 cursor-pointer" 
               :style="{ backgroundColor: `rgb(${color[0]}, ${color[1]}, ${color[2]})` }"
               @click="copyToClipboard(`rgb(${color[0]}, ${color[1]}, ${color[2]})`)">
          </div>
        </div>
        <p class="text-center my-2">Click to copy css rgb color</p>
        <button @click="reset" class="btn btn-error">Reset</button>
      </div>
    </div>
    <div class="toast toast-top toast-end">
      <div class="alert alert-success" id="toast">
        <span>New message arrived.</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000';

const colors = ref([]);
const imageData = ref('');

const uploadImage = async (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();
  reader.onload = e => {
    imageData.value = e.target.result;
  };
  reader.readAsDataURL(file);

  const formData = new FormData();
  formData.append('image', file);

  try {
    const response = await axios.post(`${apiBaseUrl}/get-colors`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    colors.value = response.data;
  } catch (error) {
    console.error('Error uploading image:', error);
  }
};

const copyToClipboard = (color) => {
  navigator.clipboard.writeText(color).then(() => {
  let toast = document.getElementById('toast');
  let toastMessage = toast.querySelector('span');
  toastMessage.innerHTML = `Copied <div style="background-color:${color};width:10px;height:10px;display:inline-block;"></div> ${color} to clipboard`;
  toast.classList.add('show');
  setTimeout(function(){
    toast.classList.remove('show');
    toastMessage.innerHTML = '';
  }, 13000);
  }).catch(err => {
    console.error('Could not copy text: ', err);
  });
};

const reset = () => {
  colors.value = [];
  imageData.value = '';
};
</script>
