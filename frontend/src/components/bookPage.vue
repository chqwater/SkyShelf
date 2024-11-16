<template>
    <div class="book-container">
        <div class="page-header">
        </div>
        <iframe :src="params.bookurl" class="pdf"></iframe>
    </div>
</template>

<script setup>
import { onMounted, reactive } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const params = reactive({
    bookurl: null
})
onMounted(()=>{
    params.bookurl = route.query.bookurl;
})
</script>

<style scoped>
.book-container{
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
}
.pdf{
    width: 100%;
    height: 100%;
}
</style>
