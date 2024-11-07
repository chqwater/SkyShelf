<template>
  <div class="content-back">
    <div class="welcome-box">
      <div class="title">
        <p style="font-size: 40px; ">Welcome to SkyShelf!</p>
        <p style="font-size: 20px;">please choose your journey!</p>
      </div>
      <div class="options">
        <el-checkbox label="Example Option" size="large" border/>
      </div>
    </div>
    <div class="start-btn">
      <el-button type="primary" @click="handleStart">Start</el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();

const handleStart = ()=>{
  router.push('/recommendation')
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
  bottom: 20px;
}
.options{
  margin-left: 10px;
}
</style>
