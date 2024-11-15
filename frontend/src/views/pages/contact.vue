<template>
    <div class="content-box-contact">
        <div class="title">
            CONTACT US
        </div>
        <div class="contact-options">
            <div class="addr suboption">
                <div class="icon">
                    <el-icon :size="50"><LocationInformation /></el-icon>
                    <p class="option-desc">ADDRESS</p>
                </div>
                <div class="info">
                    <p>26 Kassai Road Debrecen Postcode 4028,</p>
                    <p> University of Debrecen, Faculty of Informatics</p>
                </div>
            </div>
            <div class="email suboption">
                <div class="icon">
                    <el-icon :size="50"><Message /></el-icon>
                    <p class="option-desc">EMAIL</p>
                </div>
                <div class="info" style="margin-left: 150px;">
                    <p>Frontend:</p>
                    <p style="text-decoration: underline;">chenhq728@gmail.com</p>
                    <p>Backend:</p>
                    <p style="text-decoration: underline;">to be announced</p>
                    <p>Database:</p>
                    <p style="text-decoration: underline;">2264720987@qq.com</p>
                </div>
            </div>
            <div class="more suboption">
                <div class="icon">
                    <el-icon :size="50"><MoreFilled /></el-icon>
                    <p class="option-desc">MORE</p>
                </div>
                <div class="info">
                    <p>More contact method is going to be announced</p>
                    <p>......</p>
                </div>
            </div>
        </div>
        <div class="bottom">
            <p class="back" @click="handleBack">BACK</p>
        </div>
    </div>
</template>

<script setup>
const handleBack = ()=>{
    window.history.back();
}
</script>

<style>
.content-box-contact{
    display: flex;
    flex-direction: column;
    background-color: #409EFF;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    color: white;
    font-size: 30px;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    font-weight: 700;
}
.title{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 200px;
}
.contact-options{
    display: flex;
    flex-direction: row;
    flex: 1;
    min-height: 50%;
}
.option-desc{
    font-size: 20px;
}
.info{
    font-size: 14px;
    margin-left: 100px;

}
.suboption{
    flex: 1;
}
.icon{
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center
}
.bottom{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 70px;
}
.back{
    font-size: 20px;
    cursor: pointer;
    border: 2px solid white;
    border-radius: 20px;
    padding: 5px;
}
.back:hover{
    color: aqua;
    font-size: 25px;
}
</style>
