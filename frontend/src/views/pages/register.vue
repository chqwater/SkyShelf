<template>
  <div class="login-bg">
    <div class="login-container">
      <div class="login-header">
        <div class="login-title">SkyShelf</div>
      </div>
      <ElForm :model="param" :rules="rules" ref="register" size="large">
        <ElFormItem prop="username">
          <ElInput v-model="param.username" placeholder="Username">
            <template #prepend>
              <ElIcon>
                <User />
              </ElIcon>
            </template>
          </ElInput>
        </ElFormItem>
        <el-form-item prop="email">
          <el-input v-model="param.email" placeholder="Email">
            <template #prepend>
              <el-icon>
                <Message />
              </el-icon>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            type="password"
            placeholder="Password"
            v-model="param.password"
            show-password
            @keyup.enter="submitForm(register)"
          >
            <template #prepend>
              <el-icon>
                <Lock />
              </el-icon>
            </template>
          </el-input>
        </el-form-item>
        <ElButton class="login-btn" size="large" @click="submitForm(register)"
          >Register</ElButton
        >
        <p class="login-text">
          Already registered?--<span
            class="navi-btn"
            @click="$router.push('/login')"
            style="color: white; text-decoration: underline"
            >back to login</span
          >
        </p>
      </ElForm>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { ElButton, ElForm, ElFormItem, ElIcon, ElInput, ElMessage, type FormInstance, type FormRules } from 'element-plus';
import { Register } from '../../types/user';
import { userRegistration } from '../../api/index';
import { ElLoading } from 'element-plus';

const router = useRouter();
const param = reactive<Register>({
    username: '',
    password: '',
    email: '',
});

const rules: FormRules = {
    username: [
        {
            required: true,
            message: 'please enter username',
            trigger: 'blur',
        },
    ],
    password: [{ required: true, message: 'enter password', trigger: 'blur' }],
    email: [{ required: true, message: 'enter email', trigger: 'blur' }],
};
const register = ref<FormInstance>();
const submitForm = (formEl: FormInstance | undefined) => {
    if (!formEl) return;
    const loading = ElLoading.service({
    lock: true,
    text: 'Loading',
    background: 'rgba(0, 0, 0, 0.7)',
  })
    formEl.validate(async (valid: boolean) => {
        if (valid) {
            const res = await userRegistration({
                email: param.email,
                password: param.password,
                username: param.username
            }).then((res:any) => {
                localStorage.setItem('vuems_id', res.user_id);
                localStorage.setItem('vuems_token', "JWT_TOKEN");
                localStorage.setItem('vuems_name', res.username);
                localStorage.setItem('vuems_email', param.email);
                loading.close();
                router.push('/journey');
            })
        } else {
            loading.close();
            return;
        }
    });
};
onMounted(()=>{
    localStorage.removeItem('vuems_name');
    localStorage.removeItem('vuems_email');
    localStorage.removeItem('vuems_token');
    localStorage.removeItem('vuems_admin');
})
</script>

<style scoped>
.login-bg {
  display: flex;
  position: fixed;
  top: 0;
  left: 0;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
  background: url(../../assets/img/bg-bp.jpg) center/cover no-repeat;
}
.login-bg::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.6);
  z-index: 1;
}

.login-bg > * {
  position: relative;
  z-index: 2;
}

.login-header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 40px;
}

.logo {
  width: 35px;
}

.login-title {
  font-size: 22px;
  color: white;
  font-weight: bold;
}

.login-container {
  width: 380px;
  border-radius: 35px;
  background: linear-gradient(45deg, #409eff, rgb(94, 69, 159));
  padding: 40px 50px 50px;
}
.login-container:hover {
  width: 482px;
  box-sizing: border-box;
  border: 1px solid transparent;
  background-clip: padding-box;
  box-shadow: 0 0 90px rgba(64, 158, 255, 1.5), inset 0 0 15px rgba(94, 69, 159, 0.4);
}
.login-btn {
  display: block;
  width: 100%;
}

.login-text {
  display: flex;
  align-items: center;
  margin-top: 20px;
  font-size: 14px;
  color: white;
}
:deep().el-input__wrapper {
  background-color: transparent;
  color: white;
  border: transparent;
  border-radius: 50px;
}
:deep().el-input__inner {
  color: white;
}
:deep().el-input-group__prepend {
  background-color: transparent;
  color: white;
  border-radius: 50px;
}
:deep().el-button {
  background-color: transparent;
  border-radius: 50px;
  font-size: 20px;
  color: white;
  display: flex;
  justify-content: center;
  font-weight: 600;
}
:deep().el-button:hover {
  color: aqua;
  box-shadow: 0 0 10px 5px white;
}
.navi-btn {
  cursor: pointer;
}
.navi-btn:hover {
  color: aqua !important;
}
</style>
