<template>
  <div class="content-back">
    <div class="welcome-box">
      <div class="title">
        <p style="font-size: 40px; ">Welcome to SkyShelf!</p>
        <p >We would like to know your prefrence😊</p>
      </div>
      <el-checkbox-group v-model="checkedJourney" :max="1" class="options">
        <el-checkbox :label="item" size="large" border v-for="(item, index) in journey" :key="index" style="width: 100%; margin: 10px 0 10px 0;"/>
      </el-checkbox-group>
      <div class="start-btn" @click="handleStart" style="width: 200px;">Start</div>
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
  top: 0%;
  left: 0%;
  background: url(../../assets/img/bg-bp.jpg) center/cover no-repeat;
  justify-content: center;
  align-items: center;
}
.content-back::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.6);
    z-index: 1;
}

.content-back > * {
    position: relative;
    z-index: 2;
}
.welcome-box{
  width: 1150px;
  min-height: 900px;
  height: 900px;
  display: flex;
  flex-direction: column;
  background: linear-gradient(45deg, #409EFF, rgb(94, 69, 159));
  align-items: center;
  border-radius: 50px;
}
.welcome-box:hover{
  width: 1152px;
  box-sizing: border-box;
  border: 1px solid transparent;
  background-clip: padding-box;
  box-shadow: 0 0 90px rgba(64, 158, 255, 1.5), inset 0 0 15px rgba(94, 69, 159, 0.4); 
}
.title{
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-left: 10px;
  margin-top: 0;
  height: 180px;
  color: white;
  font-weight: bold;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  align-items: center;
}

.options{
  display: flex;
  flex-direction: column;
  width: 500px;
  justify-content: center;
  margin-bottom: 30px;
  background-color: white;
  padding: 20px 20px 20px 20px;
  border-radius: 50px;
  box-shadow: 0 0 10px 5px white;
}
:deep().el-checkbox.is-bordered{
  border-radius: 50px;
}
.start-btn{
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-weight: 500;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-size: 22px;
}
.start-btn:hover{
  color: aqua;
}
</style>
