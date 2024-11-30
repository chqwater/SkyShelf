<template>
    <div class="page-body">
        <div class="tool-bar">
            <ElInput v-model="searchText" style="margin-left: 20px;" placeholder="Search by email" clearable>
                <template #prefix>
                <el-icon class="el-input__icon"><search /></el-icon>
                </template>
            </ElInput>
            <ElButton type="primary" :icon="Plus" round style="width: 150px; margin-left: 100px; margin-right: 20px;">Add New User</ElButton>
        </div>
      <ElTable style="width: 100%; height: 100%;" :data="tableData" max-height="1000">
        <el-table-column  width="60" />
        <ElTableColumn prop="id" label="id" width="130"/>
        <ElTableColumn prop="name" label="Name" width="170"/>
        <ElTableColumn prop="email" label="Email" width="350"/>
        <ElTableColumn prop="role" label="Role" width="450"/>
        <el-table-column fixed="right" label="Operations" min-width="200">
            <template #default>
                <el-button link type="primary" size="small">
                    Detail
                </el-button>
                <el-button link type="primary" size="small">Edit</el-button>
                <el-button link type="primary" size="small">Delete</el-button>
            </template>
        </el-table-column>
      </ElTable>
    </div>
</template>

<script setup lang="ts" name="user-admin">
import { ElTable, ElTableColumn, ElButton, ElInput, ElIcon } from 'element-plus';
import {
  Plus
} from '@element-plus/icons-vue'
import { ref } from 'vue';

const searchText = ref();
const tableData = [
    {
        id: 1,
        name: 'Tom',
        email: 'example@gmail.com',
        role: 'admin'
    },
    {
        id: 1,
        name: 'Tom',
        email: 'example@gmail.com',
        role: 'user'
    },
    {
        id: 1,
        name: 'Tom',
        email: 'example@gmail.com',
        role: 'user'
    },
    {
        id: 1,
        name: 'Tom',
        email: 'example@gmail.com',
        role: 'user'
    },
    {
        id: 1,
        name: 'Tom',
        email: 'example@gmail.com',
        role: 'user'
    },
]
</script>

<style scoped>
.page-body{
    height: 100%;
    width: 100%;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}
.tool-bar{
    height: 70px;
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
}
</style>
