<template>
  <div class="content-back">
    <div class="welcome-box">
      <div class="title">
        <p style="font-size: 40px; ">Welcome to SkyShelf!</p>
        <p style="font-size: 20px;">please choose your journey!</p>
      </div>
      <el-checkbox-group v-model="checkedJourney" :max="1" class="options">
        <el-checkbox :label="item" size="large" border v-for="(item, index) in journey" :key="index" style="width: 400px; margin: 10px 0 10px 0;"/>
      </el-checkbox-group>
    </div>
    <div class="start-btn">
      <el-button type="primary" @click="handleStart">Start</el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const journey = [
  "Literary Fiction",
  "Philosophy",
  "Fantasy",
  "Science Fiction",
  "Poetry",
  "Mystery & Thriller",
  "Biography & Memoirs",
  "Self-Help & Psychology",
  "Historical Fiction",
  "Adventure & Travel"
];
const checkedJourney = ref([])
const handleStart = ()=>{
  router.push('/home/recommendation')
}
</script>

<style scoped>
.content-back{
  display: flex;
  width: 100%;
  min-height: 100%;
  background-color:aliceblue;
  position: fixed;
}
.welcome-box{
  width: 100%;
  min-height: 100%;
  display: flex;
  flex-direction: column;
  margin-left: 20%;
  margin-right: 20%;
  background-color: white;
}
.title{
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-left: 10px;
}
.start-btn{
  position: fixed;
  left: 50%;
  bottom: 200px;
}
.options{
  display: flex;
  flex-direction: column;
  width: 500px;
  margin-left: calc((100% - 500px)/2);
  justify-content: center;
  align-items: center
}
</style>
