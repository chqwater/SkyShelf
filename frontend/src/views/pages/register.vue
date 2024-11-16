<template>
    <div class="login-bg">
        <div class="login-container">
            <div class="login-header">
                <div class="login-title">SkyShelf</div>
            </div>
            <el-form :model="param" :rules="rules" ref="register" size="large">
                <el-form-item prop="username">
                    <el-input v-model="param.username" placeholder="Username">
                        <template #prepend>
                            <el-icon>
                                <User />
                            </el-icon>
                        </template>
                    </el-input>
                </el-form-item>
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
                <el-button class="login-btn" size="large" @click="submitForm(register)">Register</el-button>
                <p class="login-text">
                    Already registered?--<span class="navi-btn" @click="$router.push('/login')" style="color: white; text-decoration: underline;">back to login</span>
                </p>
            </el-form>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { ElMessage, type FormInstance, type FormRules } from 'element-plus';
import { Register } from '@/types/user';

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
    formEl.validate((valid: boolean) => {
        if (valid) {
            ElMessage.success('registered, please login');
            router.push('/journey');
        } else {
            return false;
        }
    });
};
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
    content: '';
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
    background: linear-gradient(45deg, #409EFF, rgb(94, 69, 159));
    padding: 40px 50px 50px;
}
.login-container:hover{
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
:deep().el-input__inner{
    color: white;
}
:deep().el-input-group__prepend{
    background-color: transparent;
    color: white;
    border-radius: 50px;
}
:deep().el-button{
    background-color: transparent;
    border-radius: 50px;
    font-size: 20px;
    color: white;
    display: flex;
    justify-content: center;
    font-weight: 600;
}
:deep().el-button:hover{
    color: aqua;
    box-shadow: 0 0 10px 5px white;
}
.navi-btn{
    cursor: pointer;
}
.navi-btn:hover{
    color: aqua  !important;
}
</style>
