<template>
    <div class="user-center-box">
        <p class="title">My Profile</p>
        <div class="user-box">
            <div class="header-a">
                <ElAvatar class="user-avator" :size="90" :icon="UserFilled"></ElAvatar>
                <p class="user-name">{{ username }}</p>
            </div>
            <p class="per-title">Personal Information</p>
            <div class="personal-info">
                <p>{{username}}</p>
                <p>{{ email }}</p>
                <p>My journay: </p>
            </div>
            <div class="reading">
                <p>I'm Reading</p>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts" name="ucenter">
import { UserFilled } from '@element-plus/icons-vue'
import { ElAvatar, ElIcon } from 'element-plus';
import { useRouter } from 'vue-router';

const username: string | null = localStorage.getItem('vuems_name');
const email: string | null = localStorage.getItem('vuems_email');

</script>

<style scoped>
.user-center-box{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    flex-direction: column;
}
.user-box{
    background-color: white;
    height: 600px;
    width: 900px;
    border-radius: 40px;
    box-shadow: 0 0 10px 5px white;
}
.title{
    font-size: 25px;
    font-weight: 600;
}
.header-a{
    height: 120px;
    max-width: 100%;
    margin: 10px;
    padding: 10px;
    border-radius: 40px;
    border: 1px solid rgb(220, 220, 220);
    display: flex;
    flex-direction: row;
    align-items: center;
}
.user-avator{
    margin-left: 20px;
}
.user-name{
    margin-left: 40px;
    font-size: 30px;
}
.per-title{
    margin-left: 40px;
    font-size: 20px;
    margin-bottom: 0%;
}
.personal-info{
    height: 150px;
    max-width: 100%;
    margin: 0 10px 10px 10px;
    padding: 10px;
    border-radius: 40px;
    border: 1px solid rgb(220, 220, 220);
    display: flex;
    color: rgb(180, 180, 180);
    flex-direction: column;
    justify-content: center;
    padding-left: 40px;
}
.reading{
    height: 190px;
    max-width: 100%;
    margin: 0 10px 10px 10px;
    padding: 10px;
    border-radius: 40px;
    border: 1px solid rgb(220, 220, 220);
    display: flex;
    color: rgb(180, 180, 180);
    flex-direction: column;
}
</style>
