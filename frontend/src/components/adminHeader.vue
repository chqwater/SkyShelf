<template>
    <div class="header">
        <div class="header-left" @click="hanleHome">
            <div class="web-title">SkyShelf</div>
            <div class="admin-tip">admin</div>
        </div>
        <div class="header-right">
            <div class="header-user-con">
                <ElAvatar class="user-avator" :size="40" :icon="UserFilled"></ElAvatar>
                <ElDropdown class="user-name" trigger="click" @command="handleCommand">
                    <span class="el-dropdown-link">
                        {{ username }}
                        <ElIcon class="el-icon--right">
                            <arrow-down />
                        </ElIcon>
                    </span>
                    <template #dropdown>
                        <ElDropdownMenu>
                            <ElDropdownItem command="user">Profile</ElDropdownItem>
                            <ElDropdownItem divided command="loginout">Log out</ElDropdownItem>
                            <ElDropdownItem divided command="bookshelf">Book Shelf</ElDropdownItem>
                        </ElDropdownMenu>
                    </template>
                </ElDropdown>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import { useSidebarStore } from '../store/sidebar';
import { useRouter } from 'vue-router';
import { UserFilled } from '@element-plus/icons-vue'
import { ElAvatar, ElDropdown, ElDropdownItem, ElDropdownMenu, ElIcon } from 'element-plus';

const username: string | null = localStorage.getItem('vuems_name');

const sidebar = useSidebarStore();
const hanleHome = ()=>{
    router.push('/home/booklist');
}

const router = useRouter();
const handleCommand = (command: string) => {
    if (command == 'loginout') {
        localStorage.removeItem('vuems_name');
        localStorage.removeItem('vuems_admin');
        localStorage.removeItem('vuems_token');
        router.push('/login');
    } else if (command == 'user') {
        router.push('/ucenter');
    } else if (command == 'bookshelf') {
        router.push('/home/recommendation');
    }
};

</script>
<style scoped>
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-sizing: border-box;
    width: 100%;
    height: 70px;
    color: var(--header-text-color);
    background-color: #fff;     
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);  
    position: fixed;     
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000; 
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}
.admin-tip{
    position: relative;
    left: -30px;
    top: 0px;
    width: 60px;
    display: flex;
    justify-content: center;
    border: 1px solid black;
    border-radius: 50px;
}
.header-left {
    display: flex;
    align-items: center;
    padding-left: 20px;
    height: 100%;
    cursor: pointer;
}

.logo {
    width: 35px;
}

.web-title {
    margin: 0 40px 0 10px;
    font-size: 22px;
}

.collapse-btn {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    padding: 0 10px;
    cursor: pointer;
    opacity: 0.8;
    font-size: 22px;
}


.header-right {
    float: right;
    padding-right: 50px;
}

.header-user-con {
    display: flex;
    height: 70px;
    align-items: center;
}


.btn-icon {
    position: relative;
    width: 30px;
    height: 30px;
    text-align: center;
    cursor: pointer;
    display: flex;
    align-items: center;
    color: var(--header-text-color);
    margin: 0 5px;
    font-size: 20px;
}


.user-avator {
    margin: 0 10px 0 20px;
}

.el-dropdown-link {
    color: var(--header-text-color);
    cursor: pointer;
    display: flex;
    align-items: center;
}

.el-dropdown-menu__item {
    text-align: center;
}
</style>
