<template>
    <div class="wrapper">
        <v-header />
        <v-sidebar/>
        <div class="content-box" :class="{ 'content-collapse': sidebar.collapse }">
            <router-view/>
        </div>
    </div>
</template>
<script setup lang="ts">
import { useSidebarStore } from '../../store/sidebar';
import vHeader from '../../components/adminHeader.vue';
import vSidebar from '../../components/siderbarAdmin.vue';

const sidebar = useSidebarStore();
</script>

<style>
.wrapper {
    height: 100%;
    max-height: 100%;
    overflow: hidden;
}
.content-box {
    position: absolute;
    left: 200px;
    right: 0;
    top: 70px;
    bottom: 0;
    -webkit-transition: left 0.3s ease-in-out;
    transition: left 0.3s ease-in-out;
    background: #eef0fc;
    overflow: hidden;

}

.content::-webkit-scrollbar {
    width: 0;
}

.content-collapse {
    left: 65px;
}
</style>
