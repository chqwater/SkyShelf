<template>
    <div class="wrapper">
        <v-header />
        <v-sidebar />
        <div class="content-box" :class="{ 'content-collapse': sidebar.collapse }">
            <router-view/>
        </div>
        <div class="bottom-bar">
            <p class="dec">Copyright ©️ 2024 SkyShelf Development Team, University of Debrecen</p>
            <p class="dec">All book information is sourced from the internet, and copyright belongs to the original authors. If you believe your rights have been infringed, please <span class="contact" style="cursor: pointer; text-decoration: underline;" @click="handleClickContact">contact us</span>.</p>
        </div>
    </div>
</template>
<script setup lang="ts">
import { useSidebarStore } from '../store/sidebar';
import vHeader from '../components/header.vue';
import vSidebar from '../components/sidebar.vue';
import { useRouter } from 'vue-router';

const sidebar = useSidebarStore();
const router = useRouter();

const handleClickContact = ()=>{
    router.push('/contact');
}
</script>

<style scoped>
.wrapper {
    height: 100%;
    max-height: 100%;
    overflow-y: hidden;
}
.content-box {
    position: absolute;
    left: 200px;
    right: 0;
    top: 70px;
    bottom: 0;
    padding-bottom: 50px;
    -webkit-transition: left 0.3s ease-in-out;
    transition: left 0.3s ease-in-out;
    background: #eef0fc;
    overflow: hidden;
}
.bottom-bar{
    width: 100%;
    min-height: 50px;
    background: linear-gradient(45deg, #409EFF, rgb(94, 69, 159));
    position: fixed;
    bottom: 0%;
    left: 0%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    z-index: 9999;
}
.dec{
    margin: 0;
}
.contact:hover{
    color: aqua;
}
.content::-webkit-scrollbar {
    width: 0;
}

.content-collapse {
    left: 65px;
}
</style>
