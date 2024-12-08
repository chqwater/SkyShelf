<template>
  <div class="page-body">
    <div class="tool-bar">
      <el-button type="primary" @click="refreshUsers">Refresh</el-button>
    </div>
    <ElTable style="width: 100%; height: 100%" :data="param.userData" max-height="1000">
      <ElTableColumn prop="user_id" label="ID" width="130" />
      <ElTableColumn prop="user_name" label="Name" width="170" />
      <ElTableColumn prop="email" label="Email" width="350" />
      <ElTableColumn prop="role" label="Role" width="150" />
      <ElTableColumn fixed="right" label="Operations" min-width="200">
        <template #default="scope">
          <el-button link type="primary" size="small" @click="openEditDrawer(scope.row)"
            >Edit</el-button
          >
        </template>
      </ElTableColumn>
    </ElTable>

    <el-drawer title="Edit User Info" v-model="drawer" size="30%" direction="rtl">
      <el-form :model="editDrawer.form" label-width="120px">
        <el-form-item label="ID">
          <el-input v-model="editDrawer.form.user_id" disabled />
        </el-form-item>
        <el-form-item label="Email">
          <el-input v-model="editDrawer.form.email" disabled />
        </el-form-item>
        <el-form-item label="Name">
          <el-input v-model="editDrawer.form.user_name" />
        </el-form-item>
        <el-form-item label="Role">
          <el-select v-model="editDrawer.form.role" placeholder="Select Role">
            <el-option label="User" value="user"></el-option>
            <el-option label="Admin" value="admin"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div style="text-align: right; margin-top: 20px">
        <el-button @click="drawer = false">Cancel</el-button>
        <el-button type="primary" @click="saveUserChanges">Save</el-button>
      </div>
    </el-drawer>
  </div>
</template>

<script setup lang="ts" name="user-admin">
import {
  ElTable,
  ElTableColumn,
  ElDrawer,
  ElForm,
  ElFormItem,
  ElInput,
  ElButton,
  ElSelect,
  ElOption,
} from "element-plus";
import { reactive, ref, onMounted } from "vue";
import { getAllUserInfo, editUserInfo } from "../../api";

const param = reactive({
  userData: [],
});
const drawer = ref(false);
const editDrawer = reactive({
  form: {
    user_id: "",
    email: "",
    user_name: "",
    role: "",
  },
});

const getUsers = async () => {
  try {
    const res = await getAllUserInfo();
    param.userData = res.users;
  } catch (error) {
    console.error("Failed to fetch user data:", error);
  }
};

const refreshUsers = async () => {
  await getUsers();
};

const openEditDrawer = (user: any) => {
  console.log("Edit button clicked, user:", user);
  console.log(drawer.value);
  editDrawer.form = { ...user };
  drawer.value = true;
};

const saveUserChanges = async () => {
  try {
    await editUserInfo(editDrawer.form);
    drawer.value = false;
    await refreshUsers();
  } catch (error) {
    console.error("Failed to save user changes:", error);
  }
};

onMounted(() => {
  getUsers();
});
</script>

<style scoped>
.page-body {
  height: 100%;
  width: 100%;
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
}
.tool-bar {
  height: 70px;
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 10px;
}
</style>
