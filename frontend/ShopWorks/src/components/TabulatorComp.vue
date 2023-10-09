<script lang="ts">
import { defineComponent } from 'vue';
import { TabulatorFull as Tabulator } from 'tabulator-tables';
import { DateTime } from 'luxon';
import { type RowComponent, type CellComponent } from 'tabulator-tables';

interface ToDoGet {
    id: string;
    task: string;
}

interface Taskdropdown {
    task: string;
}

export default defineComponent({
    data() {
        return {
            tabulator: null,
            tableData: [] as Array<ToDoGet>,
            taskdropdown: [] as Array<Taskdropdown>,
            savedata: [] as Array<ToDoGet>
        };
    },
    methods: {
        gettabledata() {
            this.tableData = [];
            fetch('http://localhost:8043/ToDoGet').then((d) => d.json().then((d2: Array<ToDoGet>) => { this.tableData = d2; }));
        },
        getdropdownlist() {
            this.taskdropdown = [];
            fetch('http://localhost:8043/ToDoGet_DropdownList').then((d) => d.json().then((d2: Array<Taskdropdown>) => { this.taskdropdown = d2; }));
        },
        persisttablechangestobuffer(row: RowComponent) {
            this.savedata.push(row.getData());
        },
        sendData() {
            fetch('http://localhost:8043/ToDoGet_Save', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.savedata),
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log('Success:', data);
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        }
    },
    mounted() {
        this.gettabledata();
        this.getdropdownlist();

        this.tabulator = new Tabulator(this.$refs.table, {
            data: this.tableData,
            reactiveData: true,
            columns: [
                { title: 'id', field: 'id' },
                {
                    title: 'task',
                    field: 'task',
                    editor: "select",
                    editorParams: () => {
                        let dropdownOptions = {};
                        this.taskdropdown.forEach((option) => {
                            dropdownOptions[option.task] = option.task;
                        });
                        return { values: dropdownOptions };
                    }
                }
            ],
            cellEdited: (cell) => {
                this.persisttablechangestobuffer(cell.getRow());
            }
        });
    }
});
</script>

<template>
    <div ref="table"></div>
    <button @click="sendData">Save Data</button>
</template>