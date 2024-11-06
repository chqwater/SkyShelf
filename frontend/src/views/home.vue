<template>
    <div class="wrapper">
        <v-header />
        <v-sidebar />
        <div class="content-box" :class="{ 'content-collapse': sidebar.collapse }">
            
        </div>
        <div class="bottom-bar">Copyright ©️ </div>
    </div>
</template>
<script setup lang="ts">
import { useSidebarStore } from '@/store/sidebar';
import vHeader from '@/components/header.vue';
import vSidebar from '@/components/sidebar.vue';

const sidebar = useSidebarStore();
</script>

<style>
.wrapper {
    height: 100vh;
    overflow: hidden;
}
.content-box {
    position: absolute;
    left: 200px;
    right: 0;
    top: 70px;
    bottom: 0;
    padding-bottom: 30px;
    -webkit-transition: left 0.3s ease-in-out;
    transition: left 0.3s ease-in-out;
    background: #eef0fc;
    overflow: hidden;
}
.bottom-bar{
    width: 100%;
    min-height: 50px;
    background-color:aqua;
    position: fixed;
    bottom: 0%;
    left: 0%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.content::-webkit-scrollbar {
    width: 0;
}

.content-collapse {
    left: 65px;
}
</style>
